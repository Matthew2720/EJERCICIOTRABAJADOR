# Generated by Django 4.1.3 on 2022-12-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CALCULO', '0002_alter_trabajador_mes_pagado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='Total_Salario',
            field=models.BigIntegerField(null=True),
        ),
    ]
