import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	name_first = models.CharField(max_length=50)
	name_last = models.CharField(max_length=50)
	gamer_tag = models.CharField(max_length=50, blank=True)

	events = models.ManyToManyField('Event') # many users may attend an event, and a user may attend many events
	friends = models.ManyToManyField('self') # future plans: users may have many friends, and also be friends to many users

class Event(models.Model):
	host = models.ForeignKey(User) # many events may be hosted by a user

	date = models.DateTimeField('Date and time of event')
	capacity = models.IntegerField('Capacity of event', default=0)
	location = models.CharField(max_length=200)
	description = models.TextField(max_length=500, blank=True)
