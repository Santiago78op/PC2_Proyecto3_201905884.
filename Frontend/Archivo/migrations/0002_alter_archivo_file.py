# Generated by Django 4.0.4 on 2022-05-16 14:05

import Archivo.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='file',
            field=models.FileField(upload_to='archivos', validators=[Archivo.validators.validate_file_extension]),
        ),
    ]