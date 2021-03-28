from django.shortcuts import render, redirect
from .models import Registro
from .forms import RegistroForm, LoginForm
from .models import login


def registro(request):
    registros = Registro.objects.all()
    ctx={
        'registros' : registros,
    }
    return render(request, 'registro.html', ctx)

def createRegistro(request):
    if request.method == 'GET':
        form = RegistroForm()
        ctx = {
            'form': form
        }
    else:
        form = RegistroForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('Registro')

    return render(request, 'manage_registro.html', ctx)

def login_usuario(request):
    login = login.objects.all()
    ctx={
        'login': login,
    }
    return render(request, 'login.html', ctx)

def createLogin(request):
    if request.method == 'GET':
        form = LoginForm()
        ctx = {
            'form': form
        }
    else:
        form = LoginForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('Registro')

    return render(request, 'manage_login.html', ctx)
    
