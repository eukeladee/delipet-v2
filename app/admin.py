from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['rut','nombre','apellido','contraseña','comuna','direccion']
    search_fields=['rut']
    list_per_page=5

class ProductoAdmin(admin.ModelAdmin):
    list_display=['codigo','nombre','raza','stock','descripcion','precio','tipo','imagen']
    search_fields=['codigo']
    list_per_page=5

class ItemsAdmin(admin.ModelAdmin):
    list_display=['nombre_producto','precio_producto','imagen']
    search_fields=['nombre_producto']
    list_per_page=5

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Items_Carrito,ItemsAdmin)