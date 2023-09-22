from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def natal(request):
    dataAtual = datetime.datetime.now()
    if dataAtual.month == 12 and dataAtual.day == 25:
        contexto = {
            'natal': True
        }
    else:
        contexto = {
            'natal': False
        }
    return render(request,"natal.html",contexto)

def independencia(request):
    return HttpResponse("Independencia ou morte")

def tiradentes(request):
    return HttpResponse("Hojé é feriado de Tiradentes!")