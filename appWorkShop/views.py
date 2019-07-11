from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Profesor, Alumno, Taller, TallerAlumno, TallerProfesor, Asistencia
from django.contrib.auth.models import User
from .forms import TallerAlumnoForm, SugerenciasForm, AsistenciaForm

def index(request):
    return render(request, 'iworkshop/index.html', {})

def login(request):
    return render(request, 'iworkshop/login.html', {})

def home(request):
    q = request.GET.get('q','')
    p = request.GET.get('q','')
    talleresProfe = TallerProfesor.objects.filter(id_user__contains=p)
    talleres = TallerAlumno.objects.filter(id_user__contains=q)
    return render(request, 'iworkshop/home.html', {'talleres': talleres,'talleresProfe':talleresProfe})

def buscarAlum(request):
    q =request.GET.get('q','')
    asisProfe = Asistencia.objects.all()
    talleres = Taller.objects.all()
    
    return render(request, 'iworkshop/buscarAlum.html', {'talleres': talleres,'asisProfe':asisProfe})

def tomarTaller(request):
    if request.method == 'POST':
        form = TallerAlumnoForm(request.POST) 
        if form.is_valid():
            tomado = form.save()
            return redirect('home')
        else:
            form = TallerAlumnoForm()

        return render(request,'iworkshop/home.html',{'tomado':tomado})

def results(request):
    q = request.GET.get('q','')
    query = Q(nombreTaller__contains=q)
    talleres = Taller.objects.filter(query)
    return render(request, 'iworkshop/buscarAlum.html', {'talleres': talleres})

def detalleAsis(request):
    q = request.GET.get('q','')
    detail = Asistencia.objects.get(id_asistencia=q)
    return render(request,'iworkshop/detalle_asis.html',{'detail':detail})

def comm(request):
    return render(request, 'iworkshop/comm.html',{})

def sugerencia(request):
    if request.method == 'POST':
        form = SugerenciasForm(request.POST)
        if form.is_valid():
            suger = form.save()
            return redirect('home')
    return render(request, 'iworkshop/comm.html', {'suger':suger})

def perfil(request):
    user_alum = Alumno.objects.all()
    user_profe = Profesor.objects.all()
    return render(request, 'iworkshop/perfil.html', {'user_alum': user_alum, 'user_profe': user_profe})

def asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            new_soli = form.save()
            return redirect('home')
    else:
        form = AsistenciaForm()
    return render(request,'iworkshop/comm.html',{'form':form})
        