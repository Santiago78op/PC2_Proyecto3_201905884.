# Generated by Django 4.0.4 on 2022-05-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0009_alter_imagen_imagenes'),
    ]

    operations = [
        migrations.AddField(
            model_name='diccionario',
            name='imagen',
            field=models.ImageField(default='', upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagenes',
            field=models.ImageField(default='', upload_to='img'),
            preserve_default=False,
        ),
    ]