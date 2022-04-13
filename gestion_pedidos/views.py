from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def busqueda_productos(request):
   
    return render(request, "formulario_get.html")

# Metodo GET

def buscar(request):
    
    if request.GET["producto"]:
        
        prod=request.GET["producto"]
        
        if len(prod)>20:
            
            mensaje='Excedio el numero de caracteres'
        
        else:
        
            art= Articulos.objects.filter(nombre__icontains=prod)
        
            return HttpResponse (render(request,"resultado.html", {"art": art, "query": prod}))
        
    else:
        
         mensaje= 'Debe ingresar un dato valido'
        

    return HttpResponse(mensaje)


# Metodo POST

def agregar_productos(request):
    
    if request.method == 'POST':
        
        cliente= Clientes.objects.create(
            nombre= request.POST['nombre'], 
            direccion= request.POST['direccion'],
            email= request.POST['email'],
            telefono= request.POST['telefono'],
            )
        
        
        
        return render(request, "formulario_post.html")
        
    
    return render(request, "formulario_post.html")


def Barra_principal(request):
    return HttpResponse(render (request, "barra_principla.html"))





