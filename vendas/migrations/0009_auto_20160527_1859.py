# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0008_auto_20160527_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='valor_pago',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
    ]
