# Generated by Django 4.0.4 on 2022-05-28 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0006_diccionario_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diccionario',
            name='imagen',
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenes', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.documents')),
            ],
            options={
                'verbose_name': 'imagen',
                'verbose_name_plural': 'imagenes',
            },
        ),
    ]
