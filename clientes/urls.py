from django.urls import path
from . import views

urlpatterns = [
    path('ver_clientes', views.ver_cliente, name='ver_cliente')
]