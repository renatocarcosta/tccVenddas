# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referencias',
            old_name='enderecoReferencia',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='referencias',
            old_name='nomeReferencia',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='referencias',
            old_name='telefoneReferencia',
            new_name='telefone',
        ),
    ]
