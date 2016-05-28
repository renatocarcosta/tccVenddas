# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CondicoesPagamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DiasCondicoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.IntegerField(max_length=3)),
                ('referencia', models.ForeignKey(to='vendas.CondicoesPagamentos')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_pedido', models.DateField(max_length=3)),
                ('observacao', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ean', models.IntegerField(max_length=15)),
                ('descricao', models.CharField(max_length=100)),
                ('valor_venda', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('tamanho', models.CharField(max_length=3)),
                ('data_kit', models.DateField()),
                ('data_vencimento_kit', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='cliente',
            field=models.ForeignKey(to='vendas.Clientes'),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='condicao',
            field=models.ForeignKey(to='vendas.CondicoesPagamentos'),
        ),
    ]
