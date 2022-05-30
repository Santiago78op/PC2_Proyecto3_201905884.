from django.urls import path
from . import views

urlpatterns = [
    path('', views.clasificacion, name='Clasificacion'),
    path('clfecha/<fehca_cls>/', views.clasificacion_fecha, name='clfecha')
]