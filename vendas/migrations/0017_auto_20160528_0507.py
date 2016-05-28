# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0016_auto_20160528_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='total_pedido',
            field=models.DecimalField(default=0, null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
