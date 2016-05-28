# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0014_clientes_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='data_nascimento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
