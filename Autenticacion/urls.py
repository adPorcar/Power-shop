from django.urls import path
from .views import Registro, cerrar_sesion, iniciar_sesion
urlpatterns = [
    path('', Registro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
]
