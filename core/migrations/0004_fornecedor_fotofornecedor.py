# Generated by Django 4.1.3 on 2022-11-29 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tipoproduto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='fotoFornecedor',
            field=models.ImageField(null=True, upload_to='fornecedoresImg', verbose_name='Foto'),
        ),
    ]