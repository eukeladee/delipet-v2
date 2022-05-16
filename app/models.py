from distutils.command.upload import upload
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo
    class meta:
        db_table= 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=60)
    precio = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class meta:
        db_table= 'db_producto'

class Usuario(models.Model):
    rut=models.IntegerField(null=False, primary_key=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=20)
    comuna=models.CharField(max_length=30)
    direccion=models.CharField(max_length=40)

    class meta:
        db_table= 'db_usuario'

class Items_Carrito(models.Model):
    nombre_producto= models.CharField(max_length=40)
    precio_producto= models.IntegerField()
    imagen= models.ImageField(upload_to="items_carrito",null =True)

    def __str__(self):
        return self.nombre_producto

    class Meta: 
        db_table= 'db_items_carrito'