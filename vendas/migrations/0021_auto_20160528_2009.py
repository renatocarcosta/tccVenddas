# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0020_auto_20160528_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data_kit',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ean',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='quantidade',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='tamanho',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='valor_venda',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
