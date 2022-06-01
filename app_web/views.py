from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_web.models import Productos
from app_web.models import Clientes
from app_web.models import Obra_social
from app_web.forms import Alta_producto
from app_web.forms import Alta_cliente
from app_web.forms import Alta_os
# Create your views here.


def inicio(request):

    return render (request , "inicio.html")

#alta de productos
def guarda_prod(request):

    if request.method == "POST":

        mi_formulario = Alta_producto( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        
        producto = Productos( nombre_prod=datos['nombre'] , codigo_prod=datos['codigo'])
        producto.save()
        
        return render(request, "formularios.html")


    return render(request, "formularios.html")   

#busqueda de productos

def buscar_producto(request):

    return render( request, "buscar_producto.html")


def buscar_p(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        productos2 = Productos.objects.filter(nombre_prod__icontains = nombre)
        return render( request , "resultado_busqueda.html" ,  {"productos2": productos2})

    else:
        return HttpResponse("campo vacio")

#Alta de clientes

def guarda_clie(request):

    if request.method == "POST":

        mi_formulario = Alta_cliente( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        
        cliente = Clientes( nombre=datos['nombre'] , obra_social=datos['os'] , codigo_os=datos['cod_os'] , nacimiento=datos['fec'])
        cliente.save()
        
        return render(request, "formularios_clie.html")


    return render(request, "formularios_clie.html")   

#alta OS

def guarda_os(request):

    if request.method == "POST":

        mi_formulario = Alta_os( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        
        os = Obra_social( nombre=datos['nombre_os'] , codigo_os=datos['cod_os'] , nombre_prod=datos['nombre_prod'] , codigo_prod=datos['codigo_prod'])
        os.save()
        
        return render(request, "formularios_os.html")


    return render(request, "formularios_os.html") 

# busqueda clientes

def buscar_cliente(request):

    return render( request, "buscar_cliente.html")


def buscar_c(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        clientes2 = Clientes.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busquedac.html" ,  {"clientes2": clientes2})

    else:
        return HttpResponse("campo vacio")


#busqueda obra social

def buscar_os(request):

    return render( request, "buscar_os.html")


def buscar_o(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        os2 = Obra_social.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busquedao.html" ,  {"os2": os2})

    else:
        return HttpResponse("campo vacio")

