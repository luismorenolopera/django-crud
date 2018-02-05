from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    cantidad = models.IntegerField()

