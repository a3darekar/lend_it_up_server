from django.db import models
from taggit.managers import TaggableManager
from profiles.models import Profile
from .choices import StatusChoices

from django_currentuser.middleware import get_current_authenticated_user

# Create your models here.
class Category(models.Model):
	"""
	Description: Various categories for products to be sorted in
	"""
	name 		= models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	image 		= models.ImageField(upload_to='categories/')

	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Product(models.Model):
	"""
	Description: Products to be sold or lent by users 
	"""
	title 			= models.CharField(max_length=50)
	description 	= models.CharField(max_length=100)
	category 		= models.ForeignKey(Category, default=2, on_delete='CASCADE')
	quantity		= models.PositiveIntegerField(default=1)
	sell 			= models.BooleanField(default=True)
	sellingPrice	= models.PositiveIntegerField(default=0)
	productImage 	= models.ImageField(upload_to='products/', default='default.jpeg')
	seller 			= models.ForeignKey(Profile, on_delete='CASCADE')
	lendingPrice 	= models.PositiveIntegerField(default=0)
	validity		= models.PositiveIntegerField(default=1, help_text='Validity in Months')

	rating 			= models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
	tags 			= TaggableManager()
	available	 	= models.BooleanField(default=True)
	reportedCount	= models.PositiveIntegerField(default=0)
	spam			= models.BooleanField(default=False)

	class Meta:
		verbose_name='Product'
		verbose_name_plural='Products'

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.pk:
			super(Product, self).save()
		else:
			user 					= get_current_authenticated_user()
			self.seller				= Profile.objects.filter(authAccount=user).first()
			super(Product, self).save()

class Request(models.Model):
	"""
	Description: Buyer Requests
	"""
	interestedBuyer = models.ForeignKey(Profile, on_delete='CASCADE')
	buyerContact 	= models.CharField(max_length=15)
	buyerEmail  	= models.CharField(max_length=15)
	product 		= models.ForeignKey(Product, on_delete='CASCADE')
	createdAt		= models.DateTimeField(auto_now_add=True)
	status 			= models.CharField(('Request Status'), choices=StatusChoices, max_length=15, default='pending')
	description 	= models.CharField(max_length=100, default="NA", blank=True)

	class Meta:
		verbose_name = 'Request'
		verbose_name_plural = 'Requests'

	def save(self, *args, **kwargs):
		if self.pk:
			super(Request, self).save()
		else:
			user 					= get_current_authenticated_user()
			self.interestedBuyer	= Profile.objects.filter(authAccount=user).first()
			self.buyerEmail 		= user.email
			self.buyerContact 		= self.interestedBuyer.contactNo
			super(Request, self).save()