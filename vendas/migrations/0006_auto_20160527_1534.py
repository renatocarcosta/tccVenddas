# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_auto_20160527_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diascondicoes',
            name='dia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ean',
            field=models.IntegerField(),
        ),
    ]
