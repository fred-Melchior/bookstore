from django.urls import path, include
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouter()
router.register(r'order', viewsets.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]

# isso faz com que o django utilize o viewst como uma rota ofical do app