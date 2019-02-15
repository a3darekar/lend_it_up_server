from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
# Create your views here.

class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

router = DefaultRouter()

router.register('categories', CategoryViewSet,'category')
router.register('products', ProductViewSet,'product')