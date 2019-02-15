from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category
# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

router = DefaultRouter()

router.register('categories', CategoryViewSet,'category')