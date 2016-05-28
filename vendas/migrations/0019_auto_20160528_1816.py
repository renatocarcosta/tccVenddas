# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0018_importacaoprodutos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='importacaoprodutos',
            options={'verbose_name': 'importar produto', 'verbose_name_plural': 'Importa\xe7\u0101o de Produtos'},
        ),
        migrations.AddField(
            model_name='produtos',
            name='kit',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='data_kit',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='data_vencimento_kit',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='tamanho',
            field=models.CharField(max_length=10),
        ),
    ]
