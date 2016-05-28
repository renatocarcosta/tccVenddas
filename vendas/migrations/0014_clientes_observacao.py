# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0013_auto_20160528_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='observacao',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
