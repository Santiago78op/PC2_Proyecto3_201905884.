# Generated by Django 4.0.4 on 2022-05-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0007_remove_diccionario_imagen_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
