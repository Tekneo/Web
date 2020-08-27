from django.db import models

# Create your models here.
class sciencehistory(models.Model):
	scientist_name = models.CharField(max_length=10)
	scientist_DOB = models.IntegerField()
	science_discovery = models.CharField(max_length=10)
	scientist_DOD = models.IntegerField()

def __str__(self):
	return self.scientist_name
