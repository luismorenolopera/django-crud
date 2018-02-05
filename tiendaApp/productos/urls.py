from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from productos.views import ProductoView


router = DefaultRouter()
router.register(r'productos', ProductoView)

urlpatterns = [
        url(r'^', include(router.urls))
        ]
