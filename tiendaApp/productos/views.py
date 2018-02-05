from django.shortcuts import render
from rest_framework import viewsets
from productos.models import Producto
from productos.serializers import ProductoSerializer


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

