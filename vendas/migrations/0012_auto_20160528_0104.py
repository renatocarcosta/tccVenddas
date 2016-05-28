# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0011_auto_20160527_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenspedidos',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
