from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from .models import LineaPedido, Pedido
from CarroCompra.carro import Carro
from TiendaWeb.models import Producto

@login_required(login_url='autenticacion/iniciar_sesion')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = []
    for key, value in carro.carro.items():
        producto = Producto.objects.get(id=value['producto_id'])
        lineas_pedido.append(LineaPedido(
            user=request.user,
            producto_id=producto,
            pedido_id=pedido,
            cantidad_producto=value['cantidad']
        ))
    carro.limpiar_carro()
    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email=request.user.email
    )
    messages.success(request, "El pedido se realizó correctamente")
    return redirect('Tienda')

def enviar_mail(**kwargs):
    asunto = "Gracias por su pedido"
    mensaje = render_to_string(
        'pedidos/pedido.html',
        {
            'pedido': kwargs.get('pedido'),
            'lineas_pedido': kwargs.get('lineas_pedido'),
            'nombreusuario': kwargs.get('nombreusuario')
        }
    )
    mensaje_texto = strip_tags(mensaje)
    from_email = "tu_mail"
    to = kwargs.get('email')
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)