from django.db import models

# Mapeo ORM
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #especifiacmos nombre en bbdd
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return 'Titulo: %r' %(self.titulo)
