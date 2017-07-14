# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^get/', views.get_dataelements, name='get data elements'),
    url(r'^label/', views.label, name='label'),
    url(r'^get_dataelement_page/', views.get_dataelement_page, name='get dataelement page')
]
