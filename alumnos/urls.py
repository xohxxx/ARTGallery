from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('adminuser', views.adminuser, name='adminuser'),
    path('contacto', views.contacto, name='contacto'),
    path('feriado', views.feriado, name='feriado'),
    path('formadmin', views.formadmin, name='formadmin'),
    path('formulario', views.formulario, name='formulario'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('pintura1', views.pintura1, name='pintura1'),
    path('pintura2', views.pintura2, name='pintura2'),
    path('pintura3', views.pintura3, name='pintura3'),
    path('registroadmin', views.registroadmin, name='registroadmin'),
]