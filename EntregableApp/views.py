from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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