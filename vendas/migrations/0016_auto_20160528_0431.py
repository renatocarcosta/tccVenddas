# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0015_clientes_data_nascimento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movimentacoesfinaneiras',
            options={'verbose_name': 'movimenta\xe7\u0101o', 'verbose_name_plural': 'Informa\xe7\xf5es Financeiras'},
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='data_vencimento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='valor',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_pedido',
            field=models.DateField(auto_now_add=True),
        ),
    ]
