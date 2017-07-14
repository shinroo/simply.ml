# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import users
import json
# Create your models here.

class DataElement(models.Model):
    data = models.CharField(max_length=1000)
    parentset = models.ForeignKey('Dataset')

    def __str__(self):
        return json.dumps(self.toDict())

    def toDict(self):
        return {"data": self.data, "parentset": self.parentset.toDict()}


class Dataset(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(users.models.TechnicalUser)

    def __str__(self):
        return json.dumps(self.toDict())

    def toDict(self):
        return {"name": self.name, "description": self.description}

class LabelChoice(models.Model):
    name = models.CharField(max_length=200)
    parentset = models.ForeignKey(Dataset)

    def __str__(self):
        return json.dumps(self.toDict())

    def toDict(self):
        return {"name": self.name, "parentset": self.parentset.toDict()}
