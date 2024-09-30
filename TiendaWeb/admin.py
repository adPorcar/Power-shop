from django.contrib import admin
from . models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "categorias", "imagen", "disponibilidad")
    search_fields = ("nombre", "precio", "categorias")
class CatProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created", "updated")
    readonly_fields = ("created", "updated")
    search_fields = ("nombre",)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(CategoriaProducto, CatProductoAdmin)