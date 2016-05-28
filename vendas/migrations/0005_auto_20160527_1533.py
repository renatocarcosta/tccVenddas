# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_auto_20160527_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensPedidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.IntegerField()),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=6)),
                ('pedido', models.ForeignKey(to='vendas.Pedidos')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentacoesFinaneiras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_movimento', models.DateField()),
                ('data_vencimento', models.DateField()),
                ('valor', models.DecimalField(max_digits=15, decimal_places=6)),
                ('valor_pago', models.DecimalField(max_digits=15, decimal_places=6)),
                ('observacao', models.TextField(max_length=200)),
                ('tipo_movimento', models.CharField(max_length=1, choices=[(b'E', b'Entrada'), (b'S', b'Saida')])),
                ('pedido', models.ForeignKey(to='vendas.Pedidos')),
            ],
        ),
        migrations.AlterField(
            model_name='produtos',
            name='valor_venda',
            field=models.DecimalField(max_digits=15, decimal_places=6),
        ),
        migrations.AddField(
            model_name='itenspedidos',
            name='produto',
            field=models.ForeignKey(to='vendas.Produtos'),
        ),
    ]
