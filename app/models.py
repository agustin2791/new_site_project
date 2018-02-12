# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(User):

    def get_name(self):
        return ' '.join([self.first_name, self.last_name])

    class Meta:
        proxy = True
        ordering = ('first_name',)

""" EVENT Website. Users can create a new event, invite people, customize page, send notification, see list of people going, view event that you have been invited on """
class Emails(models.Model):
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class NewEvent(models.Model):
    event_name = models.CharField(max_length=150)
    date = models.DateField(auto_now=False)
    date_end = models.DateField(auto_now=False,
                                blank=True,
                                null=True)
    time_start = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    host = models.ForeignKey(UserProfile)
    location = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    guests = models.ManyToManyField(Emails)
    description = models.TextField()
    template = models.CharField(max_length=100)

    def __unicode__(self):
        return self.event_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField(blank=True,
                                       null=True)
    email = models.ForeignKey(Emails)

    def __unicode__(self):
        return self.name
