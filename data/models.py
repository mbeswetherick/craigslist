from django.db import models

class Craiglistpost(models.Model):
	price = models.IntegerField()
	title = models.TextField()
	url = models.TextField()
	date = models.TextField()
	category = models.TextField()
	query = models.TextField()
	location_wide = models.TextField()
	category = models.TextField()
	query = models.TextField()
