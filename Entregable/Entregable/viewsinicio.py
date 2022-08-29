from http.client import HTTPResponse
from django.shortcuts import render

def inicio(request):
    mensaje = "Bienvenida/o, podes agregar a mi familia a una base de datos! usa la url /hermanas o /padres para agregarlos!"
    return HTTPResponse(mensaje)
