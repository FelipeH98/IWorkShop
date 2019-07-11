from django.contrib import admin
from .models import *

admin.site.register( Colegio )
admin.site.register( Alumno )
admin.site.register( Profesor )
admin.site.register( Taller )
admin.site.register( TallerAlumno )
admin.site.register( TallerProfesor	 )
admin.site.register( TallerColegio )
admin.site.register( Sugerencias )
admin.site.register( Asistencia )