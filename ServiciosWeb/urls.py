from django.urls import path
from ServiciosWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios,name='Servicios'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
