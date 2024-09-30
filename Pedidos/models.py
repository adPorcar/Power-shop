from django.db import models
from django.contrib.auth import get_user_model
from TiendaWeb.models import Producto
from django.db.models import Sum, F, FloatField

User = get_user_model()

class Pedido(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%r' %(self.id)
    
    @property
    def total(self):
        return self.lineapedidos.all().aggregate(
            total=Sum(
                F('producto_id__precio') * F('cantidad_producto'),
                output_field=FloatField()
            )
        )['total'] or 0.0
    class Meta:
        db_table = 'pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering = ['id']
class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='lineapedidos')
    cantidad_producto = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%r unidades de %r' %(self.cantidad_producto, self.producto_id) 
    class Meta:
        db_table = 'lineapedidos'
        verbose_name='lineapedido'
        verbose_name_plural='lineapedidos'
        ordering = ['id']