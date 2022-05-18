from django.contrib import admin
from .models import Archivo, Post

# Register your models here.
class ArchivoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    
admin.site.register(Archivo,ArchivoAdmin)
admin.site.register(Post,PostAdmin)