# Generated by Django 5.0 on 2024-01-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='CUIT',
            field=models.CharField(default='000', max_length=10),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='condicion',
            field=models.CharField(max_length=30),
        ),
    ]