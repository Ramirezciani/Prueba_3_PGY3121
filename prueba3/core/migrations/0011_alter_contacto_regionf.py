# Generated by Django 4.0.4 on 2022-06-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_contacto_alter_categoriaprod_idcategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='regionF',
            field=models.IntegerField(max_length=250, verbose_name='Region de Cliente'),
        ),
    ]
