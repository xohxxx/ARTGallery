from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request, 'index.html', context)

def adminuser(request):
    context={}
    return render(request, 'adminuser.html', context)

def contacto(request):
    context={}
    return render(request, 'contacto.html', context)

def feriado(request):
    context={}
    return render(request, 'feriado.html', context)

def formadmin(request):
    context={}
    return render(request, 'formadmin.html', context)

def formulario(request):
    context={}
    return render(request, 'formulario.html', context)

def galeria(request):
    context={}
    return render(request, 'galeria.html', context)

def login(request):
    context={}
    return render(request, 'login.html', context)

def pintura1(request):
    context={}
    return render(request, 'pintura1.html', context)

def pintura2(request):
    context={}
    return render(request, 'pintura2.html', context)

def pintura3(request):
    context={}
    return render(request, 'pintura3.html', context)

def registroadmin(request):
    context={}
    return render(request, 'registroadmin.html', context)
    