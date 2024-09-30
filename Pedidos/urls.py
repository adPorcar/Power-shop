from django.urls import path
from . import views
app_name = 'Pedidos'
urlpatterns = [
    path('procesar/', views.procesar_pedido,name='procesar_pedido'),
]
