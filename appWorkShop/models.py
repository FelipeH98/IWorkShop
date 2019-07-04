from django.db import models
import datetime

# Create your models here.

class Colegio(models.Model):
    nombreColegio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombreColegio)

class Alumno(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombreCompleto = models.CharField(max_length=100)
    colegio = models.ForeignKey('Colegio', on_delete=models.CASCADE)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return str(self.rut)

class Profesor(models.Model):
    rutProfe = models.CharField(max_length=10, primary_key=True)
    nombreProfe = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.rutProfe)

class Taller(models.Model):
    idTaller = models.AutoField(primary_key=True)
    nombreTaller = models.CharField(max_length=40)
    alumno = models.ManyToManyField( Alumno )
    profesor = models.ManyToManyField( Profesor )
    colegio = models.ManyToManyField( Colegio )
    fecha = models.DateTimeField(blank=False, null=True)

    def __str__(self):
        return str(self.nombreTaller)