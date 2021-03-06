# Generated by Django 4.0.5 on 2022-06-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_producto_imagenprod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idRut', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut Persona')),
                ('nombrePer', models.CharField(max_length=50, verbose_name='Nombre Persona')),
                ('apellidoPer', models.CharField(max_length=50, verbose_name='Apellido Persona')),
                ('emailPer', models.CharField(max_length=50, verbose_name='Email Persona')),
                ('telPer', models.IntegerField(verbose_name='Telefono Persona')),
                ('direccionPer', models.CharField(max_length=50, verbose_name='Direccion ')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagenProd',
        ),
    ]
