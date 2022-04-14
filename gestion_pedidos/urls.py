"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import  path
from gestion_pedidos.views import*


urlpatterns= [
    
    path('formulario_get/', busqueda_productos, name='consultas'),
    path('buscar/', buscar),
    path('formulario_post/', agregar_productos, name="ingreso"),
    path('barra_principal/', Barra_principal, name="menu"),
    path('index/', Idex, name="index"),
    
]