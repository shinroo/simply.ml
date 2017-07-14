# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datasets.models import DataElement, LabelChoice
from users.models import EndUser
import json


# Create your models here.

# Usage of built in user class
# u = User.objects.get(username='fsmith')
# freds_department = u.employee.department



class Label(models.Model):
    user = models.ForeignKey(EndUser)
    timestamp = models.DateTimeField(auto_now_add=True)
    dataelement = models.ForeignKey(DataElement)
    labelchoice = models.ForeignKey(LabelChoice)
