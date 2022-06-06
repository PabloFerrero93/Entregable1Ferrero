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

def Papaformulario(request):
    if request.method == "POST":
        miFormulario = PapaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        edad = informacion['edad']
        nacimiento = informacion['nacimiento']
        papa = Papa(nombre = nombre, edad = edad, nacimiento = nacimiento)
        papa.save()
        return render(request, "EntregableApp/inicio.html")
    else:
        miFormulario = PapaFormulario()
    return render(request, "EntregableApp/Papaformulario.html", {'miFormulario':miFormulario})

def Mamaformulario(request):
    if request.method == "POST":
        miFormulario = MamaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        edad = informacion['edad']
        nacimiento = informacion['nacimiento']
        mama = Mama(nombre = nombre, edad = edad, nacimiento = nacimiento)
        mama.save()
        return render(request, "EntregableApp/inicio.html")
    else:
        miFormulario = MamaFormulario()
    return render(request, "EntregableApp/Mamaformulario.html", {'miFormulario':miFormulario})

def Hermanobusqueda(request):
    return render(request, "EntregableApp/Hermanobusqueda.html")

def buscar(request):
    if request.GET['hermano']:
        nombre = request.GET['hermano']
        filtrado = Hermano.objects.filter(nombre=nombre)
        return render(request, 'EntregableApp/resultadoBusqueda.html', {'nombre':nombre, 'filtrado':filtrado})
    else:
        respuesta = "El nombre no pertenece a un hermano."
    return HttpResponse(respuesta)