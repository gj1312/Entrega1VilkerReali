from django.urls import path
from . import views
urlpatterns = [
    path("" , views.inicio, name = "inicio"),
    path("alta_productos", views.guarda_prod , name="alta_productos"),
    path("buscar_producto" , views.buscar_producto),
    path("buscar_p" , views.buscar_p),
    path("alta_clientes", views.guarda_clie , name="alta_clientes"),
    path("alta_os", views.guarda_os , name="alta_os"),
    path("buscar_cliente" , views.buscar_cliente),
    path("buscar_c" , views.buscar_c),
    path("buscar_os" , views.buscar_os),
    path("buscar_o" , views.buscar_o),

]