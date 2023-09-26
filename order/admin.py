from django.contrib import admin

# Register your models here.

from .models.order import Order
from .serializers.order_serializer import OrderSerializer