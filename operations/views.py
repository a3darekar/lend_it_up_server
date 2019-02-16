from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .serializers import CategorySerializer, ProductSerializer, RequestSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Request
from profiles.models import Profile
# Create your views here.

class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
	serializer_class = ProductSerializer

	def get_queryset(self):
		user = self.request.user
		if user.is_authenticated:
			pk = self.request.query_params.get('category', None)
			if pk is not None:
				category = Category.objects.filter(pk = pk).first()
				if category:
					products = Product.objects.filter(category = category)
					return products
		return Product.objects.none()

	def create(self, request, *args, **kwargs):
		if request.method == 'POST':
			alldata			= request.POST
			category 		= alldata.get("category", "0")
			self.category 	= Category.objects.get(id=int(category))
		return super(ProductViewSet, self).create(request, *args, **kwargs)



class RequestViewSet(ModelViewSet):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer

	# def get_queryset(self):
	# 	user = self.request.user
	# 	if user.is_authenticated:
	# 		pk = self.request.query_params.get('seller', None)
	# 		if pk is not None:
	# 			profile = Profile.objects.filter(pk = pk).last()
	# 			if profile:
	# 				product = Product.objects.filter(seller = profile).first()
	# 				return Request.objects.filter(product=product)
	# 	return Request.objects.none()


router = DefaultRouter()

router.register('categories', CategoryViewSet,'category')
router.register('products', ProductViewSet,'product')
router.register('requests', RequestViewSet,'request')