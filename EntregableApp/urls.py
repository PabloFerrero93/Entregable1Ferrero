from django.urls import path
from EntregableApp.views import *

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('papa/', papa, name= "papa"),
    path('mama/', mama, name= "mama"),
    path('hermano/', hermano, name= "hermano"),
    path('Hermanoformulario/', Hermanoformulario, name= "Hermanoformulario"),
    path('Hermanobusqueda/', Hermanobusqueda, name= "Hermanobusqueda"),
    path('buscar/', buscar, name= "buscar"),
    path('Papaformulario/', Papaformulario, name= "Papaformulario"),
    path('Mamaformulario/', Mamaformulario, name= "Mamaformulario"),
]