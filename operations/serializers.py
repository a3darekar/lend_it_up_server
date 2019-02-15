from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('name', 'description', 'image')
		read_only_fields = ('name', 'description', 'image')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'quantity', 'sell', 'sellingPrice', 'lendingPrice', 'validity', 'rating', 'available', 'reportedCount', 'spam')
    