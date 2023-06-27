from django.contrib import admin
from .models import Administrador, Artista, Contacto, Sexo
# Register your models here.
admin.site.register(Administrador)
admin.site.register(Artista)
admin.site.register(Contacto)
admin.site.register(Sexo)

