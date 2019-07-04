from django.shortcuts import render
from .models import Profesor, Alumno
from django.contrib.auth.models import User

def index(request):
    return render(request, 'iworkshop/index.html', {})

def login(request):
    return render(request, 'iworkshop/login.html', {})

def home(request):
    return render(request, 'iworkshop/home.html', {})

def buscar(request):
    return render(request, 'iworkshop/buscar.html', {})

def comm(request):
    return render(request, 'iworkshop/comm.html', {})

def perfil(request):
    logged = User.objects.all()
    user_alum = Alumno.objects.all()
    user_profe = Profesor.objects.all()
    return render(request, 'iworkshop/perfil.html', {'logged': logged, 'user_alum': user_alum, 'user_profe': user_profe})