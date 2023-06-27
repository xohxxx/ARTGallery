"""
URL configuration for ARTgalery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from alumnos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/',include('alumnos.urls')),
    path('index/', views.index, name='index'),
    path('adminuser/', views.adminuser, name='adminuser'),
    path('contacto/', views.contacto, name='contacto'),
    path('feriado/', views.feriado, name='feriado'),
    path('formadmin/', views.formadmin, name='formadmin'),
    path('formulario/', views.formulario, name='formulario'),
    path('galeria/', views.galeria, name='galeria'),
    path('login/', views.login, name='login'),
    path('pintura1/', views.pintura1, name='pintura1'),
    path('pintura2/', views.pintura2, name='pintura2'),
    path('pintura3/', views.pintura3, name='pintura3'),
    path('registroadmin/', views.registroadmin, name='registroadmin'),
]
