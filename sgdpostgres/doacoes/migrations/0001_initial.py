# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigoIbge', models.CharField(max_length=7, verbose_name='Codigo IBGE')),
                ('cidade', models.CharField(max_length=200, verbose_name='Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('doador', models.CharField(max_length=100, verbose_name='Doador')),
                ('cep', models.CharField(max_length=8, null=True, verbose_name='CEP')),
                ('bairro', models.CharField(max_length=100, null=True, verbose_name='Bairro')),
                ('logradouro', models.CharField(max_length=100, null=True, verbose_name='Rua/Av/etc')),
                ('numero', models.CharField(max_length=5, null=True, verbose_name='numero')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doacoes.Cidade', verbose_name='Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='TelefonesDoador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ddd', models.CharField(max_length=3, null=True, verbose_name='DDD')),
                ('numero', models.CharField(max_length=9, verbose_name='Telefone')),
                ('ramal', models.CharField(max_length=9, null=True, verbose_name='Ramal')),
                ('doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doacoes.Doador')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de telefone')),
            ],
        ),
        migrations.AddField(
            model_name='telefonesdoador',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doacoes.TipoTelefone'),
        ),
    ]
