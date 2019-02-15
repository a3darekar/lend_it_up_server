from django.db import models
from taggit.managers import TaggableManager
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

class Product(models.Model):
	"""
	Description: Products to be sold or lent by users 
	"""
	title 			= models.CharField(max_length=50)
	description 	= models.CharField(max_length=100)
	quantity		= models.PositiveIntegerField(default=1)
	sell 			= models.BooleanField(default=True)
	sellingPrice	= models.PositiveIntegerField(default=0)

	lendingPrice 	= models.PositiveIntegerField(default=0)
	validity		= models.PositiveIntegerField(default=1, help_text='Validity in Months')

	rating 			= models.DecimalField(max_digits=3, decimal_places=2)
	tags 			= TaggableManager()
	available	 	= models.BooleanField(default=True)
	reportedCount	= models.PositiveIntegerField(default=0)
	spam			= models.BooleanField(default=False)

	class Meta:
		pass