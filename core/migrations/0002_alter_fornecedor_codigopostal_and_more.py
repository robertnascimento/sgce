# Generated by Django 4.1.3 on 2022-11-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='codigoPostal',
            field=models.IntegerField(verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.IntegerField(verbose_name='Telefone'),
        ),
    ]