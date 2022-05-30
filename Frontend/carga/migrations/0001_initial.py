# Generated by Django 4.0.4 on 2022-05-18 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=80)),
                ('documento', models.FileField(upload_to='documents')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'documents',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='Diccionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diccionario', models.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.documents')),
            ],
            options={
                'verbose_name': 'diccionario',
                'verbose_name_plural': 'diccionarios',
            },
        ),
    ]