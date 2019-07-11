from django.db import models
from datetime import datetime
DIAS_SEMANA = ( 
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),

)

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
        return str(self.rut+"|"+self.nombreCompleto)

class Profesor(models.Model):
    rutProfe = models.CharField(max_length=10, primary_key=True)
    nombreProfe = models.CharField(max_length=100, null=True, blank=True)
    apellidoProfe = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.rutProfe)

class Taller(models.Model):
    idTaller = models.AutoField(primary_key=True)
    nombreTaller = models.CharField(max_length=40)
    fecha = models.CharField(max_length=12, choices=DIAS_SEMANA, default="Lunes")
    hora_comienzo = models.TimeField (null=True, blank=True)
    duracion_total= models.CharField( max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.nombreTaller)

class TallerAlumno(models.Model):
    id_TA = models.AutoField(primary_key=True)
    id_user = models.CharField( max_length=40, null=True, blank=True)
    tallerTomado = models.ForeignKey( Taller , null=True, blank=True,on_delete=models.CASCADE)
    alumnoTomado = models.ForeignKey( Alumno , null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_user)

class TallerProfesor(models.Model):
    id_TP = models.AutoField(primary_key=True)
    id_user = models.CharField( max_length=40, null=True, blank=True)
    tallerTomado = models.ForeignKey( Taller , null=True, blank=True,on_delete=models.CASCADE)
    profesorTomado = models.ForeignKey( Profesor , null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_user)

class TallerColegio(models.Model):
    id_TC = models.AutoField(primary_key=True)
    id_user = models.CharField( max_length=40, null=True, blank=True)
    tallerTomado = models.ForeignKey( Taller , null=True, blank=True,on_delete=models.CASCADE)
    colegioTomado = models.ForeignKey( Colegio , null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_user)

class Sugerencias(models.Model):
    id_sugerencia = models.AutoField(primary_key=True)
    alumnoSeg = models.ForeignKey( Alumno , null=True, blank=True,on_delete=models.CASCADE)
    sugerencia = models.TextField(blank=True)

    def __str__(self):  
        return str(self.alumnoSeg)

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    alumnos = models.ManyToManyField(Alumno)
    profesor = models.ForeignKey( Profesor , null=True, blank=True,on_delete=models.CASCADE)
    taller = models.ForeignKey( Taller , null=True, blank=True,on_delete=models.CASCADE)
    fecha = models.DateField(default = datetime.now, blank = True)

    def __str__(self):
        return str(self.taller)