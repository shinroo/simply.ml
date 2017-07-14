# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/', views.new_dataset, name='create a new dataset'),
    url(r'^insert/', views.insert_dataelement_into_dataset, name='insert a dataelement into a dataset'),
    url(r'^add_label_choice/', views.insert_labelchoice_into_dataset, name='add a label choice')
]



