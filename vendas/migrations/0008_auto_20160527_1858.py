# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0007_auto_20160527_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenspedidos',
            name='subtotal',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='pedido',
            field=models.ForeignKey(blank=True, to='vendas.Pedidos', null=True),
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='valor',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='valor_pago',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='valor_venda',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
    ]
