# Generated by Django 4.0.4 on 2022-06-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_contacto_regionf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='regionF',
            field=models.CharField(max_length=250, verbose_name='Region de Cliente'),
        ),
    ]
