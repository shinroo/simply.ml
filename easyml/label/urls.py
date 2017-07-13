# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^create/', views.create_dataset, name='create dataset'),
	url(r'^insert/', views.insert_dataelement, name='insert data element'),
	url(r'^get/', views.get_dataelements, name='get data elements'),
	url(r'^inser_label_choice/', views.insert_labelchoice, name='inser label choice')
]