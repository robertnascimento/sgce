# Generated by Django 4.1.3 on 2022-11-29 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_fornecedor_codigopostal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
            ],
        ),
    ]
