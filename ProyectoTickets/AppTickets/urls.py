from django.urls import path
from AppTickets.views import * #inicio,partidos,socios,clubs

urlpatterns = [
    path('inicio/', inicio),
    path('inicio/', inicio, name="Inicio"),
    path('clubs/', clubs, name="Clubs"),
    path('socios/', socios,name="Socios"),
    path('partidos/', partidos, name="Partidos"),
    path('buscar/', buscar, name="Buscar"),
    path('buscarSocio/', buscarSocio, name="BuscarSocio"),
]