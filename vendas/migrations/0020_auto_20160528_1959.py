# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0019_auto_20160528_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='kit',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
