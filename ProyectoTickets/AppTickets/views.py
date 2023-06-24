from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, "AppTickets/inicio.html")

def clubs(request):
    return render(request, "AppTickets/clubs.html")

def socios(request):
    return render(request, "AppTickets/socios.html")

def partidos(request):
    return render(request, "AppTickets/partidos.html")

