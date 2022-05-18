from urllib import request
from django.db import models
from jsonfield import JSONField


# Create your models here.

class Archivo(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='archivos')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name = 'archivo'
        verbose_name_plural = 'archivos'
        
    def __str__(self):
        return self.titulo

class Post(models.Model):
    contenido = JSONField()
    archivos = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name = 'post'
        verbose_name_plural = 'posts'

