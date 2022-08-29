from datetime import *
from http.client import HTTPResponse
from django.shortcuts import render
from .models import familiar
# Create your views here.



def hermanas(request):
    hermana_1 = familiar(nombre= "Valentina",  parentesco= "Hermana", cumpleaños= date(1999, 5, 13))
    hermana_2 = familiar(nombre= "Bernardita", parentesco= "Hermana", cumpleaños= date(2002, 6, 22))
    hermana_1.save()
    hermana_2.save()
    return HTTPResponse(f"Agregaste a mis hermanas {hermana_1.nombre}  y {hermana_2.nombre} a la base de datos")

def padres(request):
    mama = familiar(nombre= "Maria Laura",  parentesco= "Madre", cumpleaños= date(1969, 7, 9))
    papa = familiar(nombre= "Marcelo", parentesco= "Padre", cumpleaños= date(1961, 10, 18))
    mama.save()
    papa.save()
    diccionario = {}
    return HTTPResponse(f"Mis viejos fueron agregados a la base de datos\n {papa.nombre}, nacimiento: {papa.cumpleaños} , {papa.parentesco}\n {mama.nombre}, nacimiento: {mama.cumpleaños} , {mama.parentesco}")


    