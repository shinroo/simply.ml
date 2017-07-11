# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import json

from label.models import Dataset, TechnicalUser, Dataelement

@csrf_exempt
def create_technical_user(request):
	if request.content_type == 'application/json': 
		reqjson = json.loads(request.body.decode("utf-8"))

		print reqjson

		user = User.objects.create_user(reqjson['username'], reqjson['email'], reqjson['password'])
		user.save()

		t = TechnicalUser(user=user)
		t.save()

		return JsonResponse({'Status':'Success'})
	else:
		return JsonResponse({'Status':'Failed'})


@csrf_exempt
def upload_dataset(request):
	if request.content_type == 'application/json': 
		reqjson = json.loads(request.body.decode("utf-8"))

		#TODO: Unghetto
		username = reqjson['username']
		password = reqjson['password']

		user = authenticate(username=username, password=password)

		if user is None:
			return JsonResponse({'Status':'Failed'})

		d = Dataset(name=reqjson['name'], description=reqjson['description'], owner=user)
		d.save()

		return JsonResponse({'Status':'Success'})
	else:
		return JsonResponse({'Status':'Failed'})

@csrf_exempt
def view_dataelement(request):
	global testjson
	return JsonResponse(testjson)