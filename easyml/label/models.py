# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import users
import json
# Create your models here.

# Usage of built in user class
# u = User.objects.get(username='fsmith')
# freds_department = u.employee.department


class DataElement(models.Model):
	data = models.CharField(max_length=1000)
	parentset = models.OneToOneField('Dataset')

class Dataset(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	owner = models.OneToOneField(users.models.TechnicalUser)

	def __str__(self):
		return json.dumps({"name":self.name,"description":self.description})

class LabelChoice(models.Model):
	name = models.CharField(max_length=200)
	parentset = models.ForeignKey(Dataset)

class Label(models.Model):
	user = models.ForeignKey(users.models.EndUser)
	timestamp = models.DateTimeField(auto_now_add=True)
	dataelement = models.ForeignKey(DataElement)
	labelchoice = models.ForeignKey(LabelChoice)
