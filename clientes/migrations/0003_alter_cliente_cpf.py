# Generated by Django 5.0.3 on 2024-03-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200804_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
