from django.db import models
from .validators import validate_file_extension

# Create your models here.
class Documents(models.Model):
    titulo = models.CharField(max_length=80)
    documento = models.FileField(upload_to='documents',validators=[validate_file_extension])
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "documents"
        verbose_name_plural = "documents"
    
    def __str__(self) -> str:
        return self.titulo

class Diccionario(models.Model):
    diccionario = models.JSONField()
    newDiccionario = models.JSONField()
    imagen = models.ImageField(upload_to='image')
    categorias = models.ForeignKey(Documents, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name = "diccionario"
        verbose_name_plural = "diccionarios"

class Imagen(models.Model):
    nombre = models.CharField(max_length=80)
    imagenes = models.ImageField(upload_to='img')
    categorias = models.ForeignKey(Documents, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name = "imagen"
        verbose_name_plural = "imagenes"