from django.urls import path
from . import views

urlpatterns = [
    path('', views.rango, name='Rango'),
    path('rangofecha/<fehca_rango>/', views.rango_fecha, name='rangofecha')
]