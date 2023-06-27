from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=200)
    contraseña = models.CharField(max_length=100)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE)

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=200)
    contraseña = models.CharField(max_length=100)    
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=200)
    telefono = models.IntegerField()
    fecha = models.DateField()
    sexo = models.BooleanField()
    descripcion = models.CharField(max_length=200)

class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=50)
