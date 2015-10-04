import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	name_first = models.CharField(max_length=50)
	name_last = models.CharField(max_length=50)
	gamer_tag = models.CharField(max_length=50, blank=True)

	events = models.ForeignKey(Event) # many users may attend an event
	friends = models.ForeignKey('self') # for future moves to make friends list

	def __str__(self):
		return self.name_first + ' ' + name_last + '/' + self.gamer_tag

class Event(models.Model):
	host = models.ForeignKey(User) # many events may be hosted by a user

	date = models.DateTimeField('Date of event')
	capacity = models.IntegerField('Capacity of event', default=0)
	location = models.CharField(max_length=200)
	description = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return str(self.host) + ':' + str(self.date)
