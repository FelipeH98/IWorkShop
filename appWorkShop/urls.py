from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('buscar', views.buscar, name='buscar'),
    path('comm', views.comm, name='comm'),
    path('perfil', views.perfil, name='perfil'),
]