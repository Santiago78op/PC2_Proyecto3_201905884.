from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar, name='Cargar'),
]