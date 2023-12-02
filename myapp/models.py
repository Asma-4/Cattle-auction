
from django.db import models



# Create your models here.

class Cow(models.Model):
	breed = models.CharField(max_length=30)
	breedsize = models.CharField(max_length=30)
	breedprice = models.CharField(max_length=30)
	#breedimage = models.ImageField(upload_to="images")


# Create your models here.
class Cattle(models.Model):
	cattle = models.CharField(max_length=35)
	cattleimage = models.CharField(max_length=35)
	cattlecolour= models.CharField(max_length=35)

