# Generated by Django 4.0.4 on 2022-05-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0005_diccionario_newdiccionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='diccionario',
            name='imagen',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]