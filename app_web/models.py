from django.db import models

# Create your models here.
class Productos(models.Model):

    nombre_prod = models.CharField(max_length=40)
    codigo_prod = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    obra_social = models.IntegerField()
    codigo_os = models.IntegerField()
    nacimiento = models.DateField()

class Obra_social(models.Model):
    nombre = models.CharField(max_length=40)
    codigo_os = models.IntegerField()
    nombre_prod = models.CharField(max_length=40)
    codigo_prod = models.IntegerField()

    