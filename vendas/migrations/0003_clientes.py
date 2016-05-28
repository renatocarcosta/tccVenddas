# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20160527_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('referencia', models.ForeignKey(to='vendas.Referencias')),
            ],
        ),
    ]
