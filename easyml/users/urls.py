# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^register_technical_user/', views.create_technical_user, name='register technical user')
]