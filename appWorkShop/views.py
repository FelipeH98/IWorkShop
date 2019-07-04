from django.shortcuts import render
from django.db.models import Q
from .models import Profesor, Alumno, Taller
from django.contrib.auth.models import User

def index(request):
    return render(request, 'iworkshop/index.html', {})

def login(request):
    return render(request, 'iworkshop/login.html', {})

def home(request):
    return render(request, 'iworkshop/home.html', {})

def buscarAlum(request):
    talleres = Taller.objects.all()
    return render(request, 'iworkshop/buscarAlum.html', {'talleres': talleres})

def results(request):
    q = request.GET.get('q','')
    query = Q(nombreTaller__contains=q)
    talleres = Taller.objects.filter(query)
    return render(request, 'iworkshop/buscarAlum.html', {'talleres': talleres})

def comm(request):
    return render(request, 'iworkshop/comm.html', {})

def perfil(request):
    user_alum = Alumno.objects.all()
    user_profe = Profesor.objects.all()
    return render(request, 'iworkshop/perfil.html', {'user_alum': user_alum, 'user_profe': user_profe})