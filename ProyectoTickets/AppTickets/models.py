from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()

class Club(models.Model):
    nombreClub = models.CharField(max_length=50)
    nombreEstadio = models.CharField(max_length=50)
    direccionEstadio = models.CharField(max_length=50)
    capacidadEstadio = models.IntegerField()

class Partido(models.Model):
    equipoLocal = models.CharField(max_length=50)
    equipoVisitante = models.CharField(max_length=50)
    fechaPartido = models.DateField()
    horarioPartido = models.TimeField()
