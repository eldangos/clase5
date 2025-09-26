from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    detalle=models.TextField()
    def __str__(self):
        return self.titulo