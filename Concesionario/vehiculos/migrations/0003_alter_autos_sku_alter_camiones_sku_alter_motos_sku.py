# Generated by Django 4.0.4 on 2022-09-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_alter_autos_sku_alter_camiones_sku_alter_motos_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='sku',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='camiones',
            name='sku',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='motos',
            name='sku',
            field=models.CharField(max_length=30),
        ),
    ]
