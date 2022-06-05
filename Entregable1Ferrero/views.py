from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def inicio(request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)