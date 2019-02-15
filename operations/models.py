from django.db import models
from taggit.managers import TaggableManager
from profiles.models import Profile
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
	quantity		= models.PositiveIntegerField(default=1)
	sell 			= models.BooleanField(default=True)
	sellingPrice	= models.PositiveIntegerField(default=0)

	lendingPrice 	= models.PositiveIntegerField(default=0)
	validity		= models.PositiveIntegerField(default=1, help_text='Validity in Months')

	rating 			= models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
	tags 			= TaggableManager()
	available	 	= models.BooleanField(default=True)
	reportedCount	= models.PositiveIntegerField(default=0)
	spam			= models.BooleanField(default=False)

	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

class Request(models.Model):
    """
    Description: Buyer Requests
    """
    interestedBuyer = models.ForeignKey(Profile, on_delete='CASCADE')
    status			= models.CharField(max_length=10)


    class Meta:
        pass