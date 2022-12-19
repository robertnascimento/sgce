from django.contrib.auth.models import AbstractUser
from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField


class Usuario(AbstractUser):
    nome = models.CharField('Nome Completo', max_length=100, blank=False)
    idade = models.IntegerField('Idade', blank=False)
    cpf = CPFField(masked=True, blank=False, unique=True)

    USERNAME_FIELD = 'cpf'

    class Meta:
        permissions = [
            ("CD", "Cadastrar,Apagar"),
            ("RU", "Lerd,Atualizar")
        ]

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    cnpj = CNPJField(masked=True, blank=False)
    telefone = models.IntegerField('Telefone', blank=False)
    codigoPostal = models.IntegerField('CEP', blank=False)
    emailFornecedor = models.EmailField('Email', max_length=100, blank=False)
    fotoFornecedor = models.ImageField(
        'Foto', upload_to='fornecedoresImg', null=True)

    def __str__(self):
        return self.nome


class TipoProduto(models.Model):
    nome = models.CharField('Nome', max_length=20, blank=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    modelo = models.CharField('Nome', max_length=30, blank=False)
    quantidade = models.IntegerField('Quantidade', blank=False)
    fotoUm = models.ImageField('Foto', upload_to='fotosProduto', blank=False)
    fotoDois = models.ImageField('Foto', upload_to='fotosProduto', blank=True)
    fotoTres = models.ImageField('Foto', upload_to='fotosProduto', blank=True)
    fotoQuatro = models.ImageField(
        'Foto', upload_to='fotosProduto', blank=True)
    fotoCinco = models.ImageField('Foto', upload_to='fotosProduto', blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo


class Retiradas(models.Model):
    quantidaderet = models.IntegerField('Quantidade', blank=False)
