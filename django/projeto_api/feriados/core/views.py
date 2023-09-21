from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def natal(request):
    contexto = {
        'natal': False
    }
    return render(request,"natal.html",contexto)

def independencia(request):
    return HttpResponse("Independencia ou morte")

def tiradentes(request):
    return HttpResponse("Hojé é feriado de Tiradentes!")