
from django.db import models

from datetime import datetime
from django.utils import timezone

# Create your models here.

class RoadSpace(models.Model):
	def __str__(self) -> str:
		return f'<Road Space No. {self.pk}>'


class RoadSpaceReservation(models.Model):
	roadSpace = models.OneToOneField(
		RoadSpace,
		on_delete=models.CASCADE,
		related_name='reservation'
	)

	encryptedTokenHash = models.CharField(max_length=255)
	
	expiryTime = models.DateTimeField(auto_now=False, auto_now_add=False) 


	def setExpiryTime(self, reservationLength: timezone.timedelta=timezone.timedelta(7)): # Placeholder default value of 7 days (1 week)
		reservationExpiryTime = timezone.now() + reservationLength

		return reservationExpiryTime


class UserGeneratedRoadSegment(models.Model):
	roadSpace = models.ForeignKey(RoadSpace, on_delete=models.SET_NULL, null=True) # Check difference between null and blank

	# All lengths are placeholders:

	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	description = models.CharField(max_length=400)

	status = models.CharField(
		max_length=50,
		choices=[
			('FR', 'for_review'),
			('PB', 'published'),
			('RJ', 'rejected')
		]
	)