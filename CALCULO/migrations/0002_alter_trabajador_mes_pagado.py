# Generated by Django 4.1.3 on 2022-12-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CALCULO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='Mes_Pagado',
            field=models.CharField(max_length=15),
        ),
    ]
