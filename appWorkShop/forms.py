from django import forms
from .models import TallerAlumno, Sugerencias, Asistencia

class TallerAlumnoForm(forms.ModelForm):
    class Meta:
        model = TallerAlumno
        fields = ('id_user','tallerTomado','alumnoTomado')

class SugerenciasForm(forms.ModelForm):
    class Meta:
        model = Sugerencias
        fields = ('alumnoSeg','sugerencia')

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['alumnos','profesor','taller',"fecha",]