# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0009_auto_20160527_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name': 'cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='condicoespagamentos',
            options={'verbose_name': 'condi\xe7\u0101o pagamento', 'verbose_name_plural': 'Condi\xe7\xf5es de Pagamento'},
        ),
        migrations.AlterModelOptions(
            name='movimentacoesfinaneiras',
            options={'verbose_name': 'movimenta\xe7\xf5es financeiras', 'verbose_name_plural': 'Movimenta\xe7\xf5es Financeiras'},
        ),
        migrations.AlterModelOptions(
            name='pedidos',
            options={'verbose_name': 'pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='produtos',
            options={'verbose_name': 'produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='referencias',
            options={'verbose_name': 'refer\xeancia', 'verbose_name_plural': 'Refer\xeancias'},
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='data_movimento',
            field=models.DateField(auto_now_add=True),
        ),
    ]
