from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<br> Página de inicio")