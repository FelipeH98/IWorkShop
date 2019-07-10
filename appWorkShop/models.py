from django.db import models

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
        return str(self.rut)

class Profesor(models.Model):
    rutProfe = models.CharField(max_length=10, primary_key=True)
    nombreProfe = models.CharField(max_length=100, null=True, blank=True)
    apellidoProfe = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.rutProfe)

class Taller(models.Model):
    idTaller = models.AutoField(primary_key=True)
    nombreTaller = models.CharField(max_length=40)
    alumno = models.ManyToManyField( Alumno , null=True, blank=True)
    profesor = models.ManyToManyField( Profesor, null=True, blank=True)
    colegio = models.ManyToManyField( Colegio , null=True, blank=True )
    fecha = models.CharField(max_length=12, choices=DIAS_SEMANA, default="Lunes")
    hora_comienzo = models.TimeField (null=True, blank=True)
    duracion_total= models.CharField( max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.nombreTaller)

class TallerAlumno(models.Model):
    id_tomado = models.AutoField(primary_key=True)
    id_user = models.CharField( max_length=40, null=True, blank=True)
    tallerTomado = models.ForeignKey( Taller , null=True, blank=True,on_delete=models.CASCADE)
    alumnoTomado = models.ForeignKey( Alumno , null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_user)