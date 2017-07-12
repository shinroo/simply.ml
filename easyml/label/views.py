# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
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
def create_dataset(request):
	if request.content_type == 'application/json': 

	#################################################################################
		reqjson = json.loads(request.body.decode("utf-8"))
		username = reqjson['username']
		password = reqjson['password']

		user = authenticate(username=username, password=password)
	#################################################################################

		if user is None:
			return JsonResponse({'Status':'Failed'})

		d = Dataset(name=reqjson['name'], description=reqjson['description'], owner=user)
		d.save()

		return JsonResponse({'Status':'Success'})
	else:
		return JsonResponse({'Status':'Failed'})

@csrf_exempt
def insert_dataelement():
	if request.content_type == 'application/json':

	#################################################################################
		reqjson = json.loads(request.body.decode("utf-8"))
		username = reqjson['username']
		password = reqjson['password']

		user = authenticate(username=username, password=password)
	#################################################################################

	if user is None:
		return JsonResponse({'Status':'Failed'})

	dataset = reqjson['dataset']
	data = reqjson['data']

	#TODO: add check

	de = Dataelement(parentset=dataset, data=data)
	de.save()

@csrf_exempt
def get_dataelements(request):

	if request.content_type == 'application/json':

	#################################################################################
		reqjson = json.loads(request.body.decode("utf-8"))
		username = reqjson['username']
		password = reqjson['password']

		user = authenticate(username=username, password=password)
	#################################################################################

	if user is None:
		return JsonResponse({'Status':'Failed'})

	dataset = reqjson['dataset']

	response = {}
	response_list = []

	results = Dataelement.objects.get(parentset=dataset)

	for result in results:
		response_list.append(result)

	response['dataelements'] = response_list

	return JsonResponse(response)

