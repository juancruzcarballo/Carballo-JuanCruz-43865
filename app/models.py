from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vino(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
         return f"{self.nombre}, {self.tipo}, {self.precio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido},  {self.email},  {self.telefono}"

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.email},  {self.telefono}"
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido},  {self.email},  {self.telefono}"


class Avatar(models.Model):
     imagen = models.ImageField(upload_to="avatares")
     user = models.ForeignKey(User, on_delete= models.CASCADE)

     def __str__(self):
         return f"{self.user} [{self.imagen}]"