
from django.shortcuts import render, redirect

from app.forms import ProductoForm
from .models import *
from .forms import *
# Create your views here.

#Seccion agregar
def agregarProducto(request):
    datos ={
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['Mensaje']= 'Producto guardado correctamente'

    return render(request, 'app/productos/agregarProducto.html',datos)

def agregarUsuario(request):
    datosU ={
        'form1' : UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datosU['Mensaje']= 'Usuario guardado correctamente'

    return render(request, 'app/usuarios/agregarUsuario.html',datosU)          

#SECCION MODIFICAR
def modificarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos ={
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['Mensaje']= 'Producto modificado correctamente'
            datos['form'] = formulario

    return render(request, 'app/productos/modificarProducto.html',datos)    

def eliminarProducto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarProductos")

def modificarUsuario(request, rut):
    usuario = Usuario.objects.get(rut=rut)
    datosU ={
        'form1' : UsuarioForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datosU['Mensaje']= 'Usuario modificado correctamente'
            datosU['form1'] = formulario

    return render(request, 'app/usuarios/modificarUsuario.html',datosU)    

def eliminarUsuario (request, rut):
    usuario = Usuario.objects.get(rut=rut)
    usuario.delete()

    return redirect(to="listarUsuario")
#SECCION LISTAR
def listarProductos(request):
    productosAll= Producto.objects.all()
    datos ={
        'listaProductos':productosAll
    }
    return render(request, 'app/productos/listarProductos.html', datos)

def listarUsuario(request):
    usuarioAll= Usuario.objects.all()
    datosU ={
        'listaUsuario':usuarioAll
    }
    return render(request, 'app/usuarios/listarUsuario.html',datosU)

def index(request):
    return render(request, 'app/index.html')

def carro(request):
    carrito = Items_Carrito.objects.all()
    datosC ={
        'listaCarrito':carrito
    }
    return render(request, 'app/carro.html',datosC)

def animalespequeños(request):
    productosAll= Producto.objects.all()
    datos ={
        'listaProductos':productosAll
    }
    return render(request, 'app/animalespequeños.html',datos)

def cuenta(request):
    usuarioAll= Usuario.objects.all()
    datosU ={
        'listaUsuario':usuarioAll
    }
    return render(request, 'app/cuenta.html',datosU)

def datos(request):
    return render(request, 'app/datos.html')

def formularioCrearCuenta(request):
    return render(request, 'app/formularioCrearCuenta.html')

def fundacion(request):
    return render(request, 'app/fundacion.html')

def gatos(request):
    productosAll= Producto.objects.all()
    datos ={
        'listaProductos':productosAll
    }
    return render(request, 'app/gatos.html',datos)

def historia(request):
    return render(request, 'app/historia.html')

def inicioSexionIni(request):
    return render(request, 'app/inicioSexionIni.html')

def perros(request):
    productosAll= Producto.objects.all()
    datos ={
        'listaProductos':productosAll
    }
    return render(request, 'app/perros.html', datos)

def seguimiento(request):
    return render(request, 'app/seguimiento.html')

def suscripcion(request):
    return render(request, 'app/suscripcion.html')

#Seccion listar
def tienda(request):
    productosAll= Producto.objects.all()
    datos ={
        'listaProductos':productosAll
    }
    if request.method == 'POST':
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()
    return render(request, 'app/tienda.html',datos)


