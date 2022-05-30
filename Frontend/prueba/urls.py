from django.urls import path
from . import views

urlpatterns = [
    path('', views.prueba, name='Prueba'),
    path('prueba/<prueba>/', views.probar, name='Probar')
]