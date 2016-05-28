# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_auto_20160527_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diascondicoes',
            old_name='referencia',
            new_name='condicao',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='referencia',
            field=models.ForeignKey(blank=True, to='vendas.Referencias', null=True),
        ),
        migrations.AlterField(
            model_name='movimentacoesfinaneiras',
            name='observacao',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='observacao',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
