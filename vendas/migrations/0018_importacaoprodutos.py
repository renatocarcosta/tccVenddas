# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0017_auto_20160528_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportacaoProdutos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'', blank=True)),
            ],
        ),
    ]
