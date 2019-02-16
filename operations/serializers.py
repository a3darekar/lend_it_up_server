from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Category, Product, Request

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model 				= Category
		fields 				= ('pk', 'name', 'description', 'image')
		read_only_fields 	= ('name', 'description', 'image')


class ProductSerializer(serializers.ModelSerializer):
	category = serializers.StringRelatedField(many = False)
	class Meta:
		model 				= Product
		fields 				= ('pk', 'title', 'category', 'description', 'seller', 'productImage', 'quantity', 'sell', 'sellingPrice', 'lendingPrice', 'validity', 'rating', 'available', 'reportedCount', 'spam')
		read_only_fields 	= ('reportedCount', 'spam', 'seller')

	def get_queryset(self):
		user = self.request.user
		if user.is_authenticated:
			pk = self.request.query_params.get('category', None)
			if category is not None:
				category = get_object_or_404(Product, pk = pk)
				return Product.objects.filter(category = category)
			else:
				Product.objects.none()
		else:
			return Product.objects.none()

	# def create(self, request, *args, **kwargs):
	# 	print(request)
	# 	# if request.POST:
	# 	# 	data = request.data
	# 	# 	category_string = request.data('category')
	# 	# 	category = Category.objects.get_object_or_404(name=category)
	# 	return super(ProductSerializer, self).update(request, *args, **kwargs)

class RequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Request
		fields 			 	= ('interestedBuyer', 'buyerContact', 'buyerEmail', 'product', 'createdAt', 'status', 'description')
		read_only_fields 	= ('interestedBuyer', 'buyerContact', 'createdAt', 'buyerContact', 'buyerEmail',)
	

