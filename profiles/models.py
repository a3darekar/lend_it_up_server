from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
	"""
	Description: Model class for User Profiles
	"""
	authAccount 	= models.OneToOneField(User, on_delete='CASCADE')
	firstName 		= models.CharField(max_length=40)
	lastName 		= models.CharField(max_length=40)
	profilePicture 	= models.ImageField(upload_to = 'profiles/')
	contactNo 		= PhoneNumberField()
	cprn 			= models.CharField(unique=True, max_length=30)
	email 			= models.EmailField(max_length=254)
	branch 			= models.CharField(max_length=30)
	academicYear 	= models.CharField(max_length=30)
	rating 			= models.DecimalField(max_digits=3, decimal_places=2)
	hasRating		= models.BooleanField(default=False)
	reviewsCount	= models.PositiveIntegerField(default=0)
	
	class Meta:
		verbose_name='Profile'
		verbose_name_plural='Profile'