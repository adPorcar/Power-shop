from django.db import models

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100) 
    precio=models.IntegerField()
    categorias=models.ForeignKey('CategoriaProducto',on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda')
    disponibilidad=models.BooleanField(default=True)
    #como mejora podria usarse stock y que eso rija la disponibilidad
    #stock=models.IntegerField() 
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    def __str__(self):
        return 'Nombre del producto: %r'%(self.nombre)
class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='categoriaProducto'
        verbose_name_plural='categoriaProductos'
    def __str__(self):
        return '%r' %(self.nombre)