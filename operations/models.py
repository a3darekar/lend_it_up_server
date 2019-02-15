from django.db import models

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