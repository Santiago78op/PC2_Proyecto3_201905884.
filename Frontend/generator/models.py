from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=100, null=True) # titulo
    document = models.FileField(upload_to='documents/xml/') #file

