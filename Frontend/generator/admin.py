from django.contrib import admin
from . import models

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Document,InfoAdmin)