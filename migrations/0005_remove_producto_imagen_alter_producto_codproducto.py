# Generated by Django 4.0.5 on 2022-06-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='producto',
            name='codProducto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo Producto'),
        ),
    ]
