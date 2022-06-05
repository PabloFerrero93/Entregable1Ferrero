from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *
from .forms import *

def inicio(request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def papa(request):
    plantilla = loader.get_template('papa.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def mama(request):
    plantilla = loader.get_template('mama.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def hermano(request):
    plantilla = loader.get_template('hermano.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def Hermanoformulario(request):
    if request.method == "POST":
        miFormulario = HermanoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        edad = informacion['edad']
        nacimiento = informacion['nacimiento']
        hermano = Hermano(nombre = nombre, edad = edad, nacimiento = nacimiento)
        hermano.save()
        return render(request, "EntregableApp/inicio.html")
    else:
        miFormulario = HermanoFormulario()
    return render(request, "EntregableApp/Hermanoformulario.html", {'miFormulario':miFormulario})