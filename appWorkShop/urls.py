from django.urls import path, re_path
from . import views 
from django.conf.urls import url, include

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('buscarAlum', views.buscarAlum, name='buscarAlum'),
    path('results', views.results, name='results'),
    path('comm', views.comm, name='comm'),
    path('perfil', views.perfil, name='perfil'),
    path('tomarTaller', views.tomarTaller, name='tomarTaller'),
    path('sugerencia', views.sugerencia, name='sugerencia'),
    path('asistencia', views.asistencia, name='asistencia'),
    path('detalleAsis', views.detalleAsis, name='detalleAsis'),

]