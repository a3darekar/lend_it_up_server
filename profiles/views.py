from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Profile
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# REST framework Router 
router = DefaultRouter() 

router.register('',ProfileViewSet,'profile')