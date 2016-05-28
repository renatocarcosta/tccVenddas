# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy
from .models import Referencias, Clientes, CondicoesPagamentos, DiasCondicoes, Produtos, Pedidos, ItensPedidos, MovimentacoesFinaneiras
# Register your models here.
admin.site.site_title = 'Gerenciamento'
#admin.site.site_header = '<img src="data:image/png;base64,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" />' 
admin.site.site_header ='Administração'
admin.site.index_title = 'Sistema de Vendas'

class ReferenciaAdmin(admin.ModelAdmin):
	search_fields = ['nome']
	list_display = ('nome', 'endereco', 'telefone')
	list_display_links = ('nome', 'endereco', 'telefone')
	pass

class ItensPedidosAdmin(admin.TabularInline):
    model = ItensPedidos
    fields = ('produto', 'quantidade')
    	

class PedidosAdmin(admin.ModelAdmin):
    search_fields = ['cliente__nome']
    inlines = [
        ItensPedidosAdmin,
    ]


class DiasCondicoesAdmin(admin.TabularInline):
    model = DiasCondicoes

class CondicoesAdmin(admin.ModelAdmin):
    inlines = [
        DiasCondicoesAdmin,
    ]

class MovimentacoesFinaneirasAdmin(admin.ModelAdmin):
    search_fields = ['data_vencimento','observacao','pedido__cliente__nome']
    list_filter = ('pedido', 'data_vencimento', 'valor_pago', 'tipo_movimento')



admin.site.register(Referencias,ReferenciaAdmin)
admin.site.register(Clientes)
admin.site.register(CondicoesPagamentos,CondicoesAdmin)
admin.site.register(Produtos)
admin.site.register(Pedidos,PedidosAdmin)
admin.site.register(MovimentacoesFinaneiras,MovimentacoesFinaneirasAdmin)
