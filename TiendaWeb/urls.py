from django.urls import path
from TiendaWeb import views

urlpatterns = [
    path('', views.tienda,name='Tienda'),
]
