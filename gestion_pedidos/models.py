from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50) #verbos_name="La direcion"-> permitira renombrar el nombre de la fila o campo de la tabla.
    email=models.EmailField(blank=True, null=True) # blank=True, null=True -> permite que el registro no sea requerrido.
    telefono=models.IntegerField(max_length=10)

    def __str__(self):
        return self.nombre



class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return self.nombre



class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

    def __str__(self):
        return self.numero
