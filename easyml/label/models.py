# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Usage of built in user class
# u = User.objects.get(username='fsmith')
# freds_department = u.employee.department

class TechnicalUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class EndUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Dataelement(models.Model):
	data = models.CharField(max_length=1000)
	parentset = models.OneToOneField('Dataset')

class Dataset(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	owner = models.OneToOneField(TechnicalUser)
	elements = models.ForeignKey(Dataelement, on_delete=models.CASCADE)