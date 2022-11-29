from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField

class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=100,blank=False)
    cnpj = CNPJField(masked=True,blank=False)
    telefone = models.IntegerField('Telefone',blank=False)
    codigoPostal = models.IntegerField('CEP',blank=False)
    emailFornecedor = models.EmailField('Email',max_length=100,blank=False)
    fotoFornecedor = models.ImageField('Foto',upload_to='fornecedoresImg',null=True)

class TipoProduto(models.Model):
    nome = models.CharField('Nome',max_length=20,blank=False)