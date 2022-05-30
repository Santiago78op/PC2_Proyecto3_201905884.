from django.contrib import admin
from .models import Documents, Diccionario, Imagen

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ("created","update")

class DiccionarioAdmin(admin.ModelAdmin):
    readonly_fields = ("created","update")
    
class ImagenAdmin(admin.ModelAdmin):
    readonly_fields = ("created","update")
    
admin.site.register(Documents, DocumentAdmin)
admin.site.register(Diccionario, DiccionarioAdmin)
admin.site.register(Imagen, ImagenAdmin)

