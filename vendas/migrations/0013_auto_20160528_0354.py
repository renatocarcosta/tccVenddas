# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0012_auto_20160528_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itenspedidos',
            options={'verbose_name': 'item do pedido', 'verbose_name_plural': 'Itens do Pedido'},
        ),
        migrations.AddField(
            model_name='pedidos',
            name='total_pedido',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
