# -*- coding: utf-8 -*-
from django.db import models, IntegrityError, transaction
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from datetime import datetime , timedelta
from decimal import *
import os
import re



# Create your models here.
class Referencias(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'referência'
        verbose_name_plural = 'Referências'

    def __str__(self):              # __unicode__ on Python 2
        return self.nome

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100,blank=True,null=True)
    telefone = models.CharField(max_length=15,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    observacao = models.CharField(max_length=100,blank=True,null=True)
    data_nascimento = models.DateField(blank=True,null=True)
    referencia = models.ForeignKey(Referencias,blank=True,null=True)                    


    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):      
        if self.referencia:
            return self.nome.upper()+' - '+self.referencia.nome.upper()
        return self.nome.upper()+' - Sem Referencia'

        
class CondicoesPagamentos(models.Model):
    descricao = models.CharField(max_length=100)                    


    class Meta:
        verbose_name = 'condiçāo pagamento'
        verbose_name_plural = 'Condições de Pagamento'

    def __str__(self):            
        return self.descricao

class DiasCondicoes(models.Model):
    dia = models.IntegerField()
    condicao = models.ForeignKey(CondicoesPagamentos)                       

    def __str__(self):            
        return str(self.dia)


class ImportacaoProdutos(models.Model):
    file = models.FileField(upload_to='', blank = True)
    def save(self, *args, **kwargs):
        super(ImportacaoProdutos, self).save(*args, **kwargs)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_ = open(os.path.join(BASE_DIR, str(self.file)),'r')
        #pd = Produtos.objects.all().update(data_vencimento_kit = datetime.now())
        #pd.save()
        #Carrega os arquivos
        codigo_kit = 0
        for line in file_:
            if line.split(',')[0]== 'Kit :':
                codigo_kit = line.split(',')[1];
            if line.split(',')[0]:
                try:
                    with transaction.atomic():
                        codigo_prod = int(line.split(',')[0])
                        vDesc=(line.split(',')[1])
                        vTam = (line.split(',')[2])
                        vQuant= 1#line.split(',')[3].replace('"','')
                        vValorVenda=(Decimal((line.split(',')[4].replace('"',''))+'.'+(line.split(',')[5].replace('"',''))))
                    
                        pr = Produtos.objects.create()
                        pr.ean=codigo_prod
                        pr.descricao=vDesc
                        pr.valor_venda=vValorVenda
                        pr.quantidade=vQuant
                        pr.tamanho=vTam
                        pr.kit=codigo_kit
                        pr.save()
                    
                except Exception, e:
                    print(e)
                    pass
                
        file_.close()
        

    class Meta:
        verbose_name = 'importar produto'
        verbose_name_plural = 'Importaçāo de Produtos'


class Produtos(models.Model):
    ean = models.IntegerField(blank=True,null=True)
    descricao = models.CharField(max_length=100,blank=True,null=True)
    valor_venda = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
    quantidade = models.IntegerField(blank=True,null=True)
    tamanho = models.CharField(max_length=10,blank=True,null=True)
    data_kit = models.DateField(auto_now_add=True,blank=True,null=True)
    data_vencimento_kit = models.DateField(blank=True,null=True)
    kit = models.CharField(max_length=20,blank=True,null=True)


    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'Produtos'
        ordering=['ean']

    def __str__(self):            
        return str(self.ean)+" - "+self.descricao+" - "+self.tamanho+" - R$ "+str(self.valor_venda)



class Pedidos(models.Model):
    data_pedido = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Clientes)
    condicao = models.ForeignKey(CondicoesPagamentos)    
    observacao = models.TextField(max_length=200,blank=True,null=True) 
    total_pedido = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True,default=0)                  
    
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):            
        return 'Ped:'+str(self.id)+' - Cli:'+str(self.cliente.nome)


class ItensPedidos(models.Model):
    pedido = models.ForeignKey(Pedidos)                     
    produto = models.ForeignKey(Produtos)  
    quantidade = models.IntegerField(default=1)
    subtotal   = models.DecimalField(max_digits=15, decimal_places=2)                   

    class Meta:
        verbose_name = 'item do pedido'
        verbose_name_plural = 'Itens do Pedido'

    def __str__(self):            
        return str(self.produto.descricao)

#
#  Procedimento para criar as movimentacoes financeiras
#
@receiver(pre_save, sender=ItensPedidos)
def atz_estoque_e_movimentacoes(sender, instance, **kwargs):
    pr = Produtos.objects.get(id=instance.produto_id)
    instance.subtotal = instance.quantidade * pr.valor_venda
    pr.quantidade -= instance.quantidade
    pr.save()
   
    pd = Pedidos.objects.get(pk=instance.pedido_id)
    pd.total_pedido += instance.subtotal

    dias = DiasCondicoes.objects.filter(condicao_id=pd.condicao.id).all()
    pd.save()
    for reg in dias:
        try:
            mv = MovimentacoesFinaneiras.objects.get(pedido_id=instance.pedido_id,observacao=reg.dia)
        except Exception, e:
            mv = MovimentacoesFinaneiras.objects.create(pedido_id=instance.pedido_id,data_vencimento=datetime.now().strftime('%Y-%m-%d'),valor=0,tipo_movimento='E',observacao=reg.dia)
 
        mv.valor += instance.subtotal / dias.count()
        mv.data_vencimento = datetime.now() + timedelta(int(reg.dia))
        mv.save()  

# Retira Saldo e retorna item para o estoque.
#
@receiver(pre_delete, sender=ItensPedidos)
def atz_estoque_atualiza(sender, instance, **kwargs):
    pr = Produtos.objects.get(id=instance.produto_id)
    instance.subtotal = instance.quantidade * pr.valor_venda
    pr.quantidade += instance.quantidade
    pr.save()

   


class MovimentacoesFinaneiras(models.Model):
    TIPO_MOVIMENTOS = (
        ('E', 'Entrada'),
        ('S', 'Saida'),
    )
    data_movimento = models.DateField(auto_now_add=True, blank=True)
    pedido = models.ForeignKey(Pedidos,blank=True,null=True)
    data_vencimento = models.DateField(blank=True,null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
    valor_pago = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    observacao = models.TextField(max_length=200,blank=True,null=True)  
    tipo_movimento = models.CharField(max_length=1, choices=TIPO_MOVIMENTOS)                    

    class Meta:
        verbose_name = 'movimentaçāo'
        verbose_name_plural = 'Informações Financeiras'

    def __str__(self):     
        if self.pedido:
            cli =  self.pedido.cliente
        else:
            cli = 'Sem Pedido'      
        return '%s - %s /Venc: %s / R$ %s' % (self.pedido_id, cli, self.data_vencimento,self.valor)






