from django.contrib import admin

# Register your models here.

from .models import Category, Product

from .serializers import CategorySerializer, ProductSerializer