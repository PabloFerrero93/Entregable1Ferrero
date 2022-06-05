
from django.contrib import admin
from django.urls import path
from Entregable1Ferrero.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name= "inicio")

]
