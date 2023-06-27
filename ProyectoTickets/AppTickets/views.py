from django.shortcuts import render
from django.http import HttpResponse
from AppTickets.forms import *
from AppTickets.models import *
# Create your views here.


def inicio(request):
    return render(request, "AppTickets/inicio.html")

def socios(request):
    if request.method == 'POST':
        miFormulario = CargaSocio(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            socio = Socio(nombre=informacion["nombre"],apellido=informacion["apellido"],dni=informacion["dni"],email=informacion["email"])
            socio.save()
            miFormulario=CargaSocio()
            return render(request,"AppTickets/socios.html",{"miFormulario":miFormulario})
    else:
        miFormulario = CargaSocio()
    return render(request, "AppTickets/socios.html",{"miFormulario":miFormulario})


def partidos(request):
    if request.method == 'POST':
        miFormulario = CargaPartido(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            partido = Partido(equipoLocal=informacion["equipoLocal"],equipoVisitante=informacion["equipoVisitante"],fechaPartido=informacion["fechaPartido"],horarioPartido=informacion["horarioPartido"])
            partido.save()
            miFormulario=CargaPartido()
            return render(request,"AppTickets/partidos.html",{"miFormulario":miFormulario})
    else:
        miFormulario = CargaPartido()
    return render(request, "AppTickets/partidos.html",{"miFormulario":miFormulario})

def clubs(request):
    if request.method == 'POST':
        miFormulario = CargaClub(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            club = Club(nombreClub=informacion["nombreClub"],nombreEstadio=informacion["nombreEstadio"],direccionEstadio=informacion["direccionEstadio"],capacidadEstadio=informacion["capacidadEstadio"])
            club.save()
            miFormulario=CargaClub()
            return render(request,"AppTickets/clubs.html",{"miFormulario":miFormulario})
    else:
        miFormulario = CargaClub()
    return render(request, "AppTickets/clubs.html",{"miFormulario":miFormulario})

def buscarSocio(request):
    return render(request, "AppTickets/buscarSocio.html")

def buscar(request):
    if request.GET["dni"]:
        dni = request.GET["dni"]
        socios = Socio.objects.filter(dni = dni)
        return render(request,"AppTickets/inicio.html",{"socios":socios})
    else:
        respuesta = "No se enviaron datos"
    
    return render (request, "AppTickets/inicio.html", {"respuesta":respuesta})
