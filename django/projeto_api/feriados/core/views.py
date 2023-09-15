from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def natal(request):
    return HttpResponse("Não é natal")

def independencia(request):
    return HttpResponse("Independencia ou morte")