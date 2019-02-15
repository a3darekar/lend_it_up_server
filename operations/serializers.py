from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model 				= Category
		fields 				= ('pk', 'name', 'description', 'image')
		read_only_fields 	= ('name', 'description', 'image')

class ProductSerializer(serializers.ModelSerializer):
	tags = TagListSerializerField()
	class Meta:
		model 				= Product
		fields 				= ('title', 'description', 'quantity', 'sell', 'sellingPrice', 'lendingPrice', 'validity', 'rating', 'available', 'tags', 'reportedCount', 'spam')
		read_only_fields 	= ('reportedCount', 'spam')