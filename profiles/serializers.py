from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin

class ProfileSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
	contactNo = serializers.CharField(
		validators=PhoneNumberField().validators
	)

	class Meta:
		model 				= Profile
		fields 				= ('pk', 'authAccount', 'firstName', 'lastName', 'profilePicture', 'contactNo', 'cprn', 'branch', 'academicYear', 'rating', 'hasRating', 'reviewsCount')
		read_only_fields 	= ('rating', 'hasRating', 'reviewsCount')
