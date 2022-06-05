
from django.contrib import admin
from django.urls import path
from Entregable1Ferrero.views import *
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('EntregableApp/', include('EntregableApp.urls'))

]
