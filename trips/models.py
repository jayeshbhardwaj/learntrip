from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Trip(models.Model):
	tripId = models.AutoField(primary_key=True)
	standardFare = models.FloatField(validators =  [MinValueValidator(0)]);
	durationHours = models.FloatField(validators =  [MinValueValidator(0)]);
	totalDistance = models.FloatField(validators =  [MinValueValidator(0)]);
	description = models.CharField(max_length=2000);
	rating = models.DecimalField(validators =  [MinValueValidator(0),MaxValueValidator(5)],max_digits=2, decimal_places=1);


	def __unicode__(self):
		return self.description

