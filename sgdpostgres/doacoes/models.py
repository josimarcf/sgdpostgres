# coding: utf-8

from django.db import models

class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    codigoibge = models.CharField(max_length=7, null=False, blank=False, verbose_name='Codigo IBGE')
    cidade = models.CharField(max_length=200, null=False, blank=False, verbose_name='Municipio')

class Doador(models.Model):
    id = models.AutoField(primary_key=True)
    doador = models.CharField(blank=False, max_length=100, verbose_name='Doador', null=False)
    cep = models.CharField(max_length=8, null=True, verbose_name='CEP')
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name='Municipio')
    bairro = models.CharField(max_length=100, null=True,verbose_name='Bairro')
    logradouro = models.CharField(max_length=100, null=True, verbose_name='Rua/Av/etc')
    numero = models.CharField(max_length=5,null=True, verbose_name='numero')

class TipoTelefone(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, null=False, verbose_name='Tipo de telefone')


class TelefonesDoador(models.Model):
    id = models.AutoField(primary_key=True)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE, null=False)
    ddd = models.CharField(max_length=3, null=True, verbose_name='DDD')
    numero = models.CharField(max_length=9, null=False, verbose_name='Telefone')
    ramal = models.CharField(max_length=9, null=True, verbose_name='Ramal')
    tipo = models.ForeignKey(TipoTelefone, on_delete=models.PROTECT)




