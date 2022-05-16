from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carro, name="carro"),
    path('Animales pequeños/', animalespequeños, name="animalespequeños"),
    path('Cuenta/', cuenta, name="cuenta"),
    path('Datos/', datos, name="datos"),
    path('Crear Cuenta/', formularioCrearCuenta, name="formularioCrearCuenta"),
    path('Fundacion/', fundacion, name="fundacion"),
    path('Gatos/', gatos, name="gatos"),
    path('Historial/', historia, name="historia"),
    path('Delipet/', inicioSexionIni, name="inicioSexionIni"),
    path('Perros/', perros, name="perros"),
    path('Seguimiento/', seguimiento, name="seguimiento"),
    path('Suscribirse/', suscripcion, name="suscripcion"),
    path('Tienda/', tienda, name="tienda"),
    path('AgregarProducto/', agregarProducto, name="agregarProducto"),
    path('ModificarProducto/<codigo>/', modificarProducto, name="modificarProducto"),
    path('EliminarProducto/<codigo>/', eliminarProducto, name="eliminarProducto"),
    path('ListarProductos/', listarProductos, name="listarProductos"),
    path('AgregarUsuario/', agregarUsuario, name="agregarUsuario"),
    path('ListarUsuario/', listarUsuario, name="listarUsuario"),
    path('ModificarUsuario/<rut>', modificarUsuario, name="modificarUsuario"),
    path('EliminarUsuario/<rut>', eliminarUsuario, name="eliminarUsuario")
]