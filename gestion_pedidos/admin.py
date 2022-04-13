from encodings import search_function
from django.contrib import admin
from gestion_pedidos.models import *


class Clientes_admin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","telefono")
    search_fields=("nombre","direccion")               # Permite agregar filtros de busqueda en el panel de admin
    
class Articulos_admin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    list_filter=("nombre","seccion","precio")           # Permite agregar filtros en secciones en el panel de admin.
    
class Pedido_admin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")         # Permite contextualizar los datos registrados de las tablas.
    list_filter=("numero","fecha","entregado")







admin.site.register(Clientes,Clientes_admin)
admin.site.register(Pedido,Pedido_admin)
admin.site.register(Articulos,Articulos_admin)




