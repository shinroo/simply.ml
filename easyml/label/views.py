# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
import json

from label.models import Dataset, Dataelement
from users.models import TechnicalUser

@csrf_exempt
def create_dataset(request):
	if request.content_type != 'application/json':
		return JsonResponse({"Status":403,"Message" :"Forbidden - Only accepts Content-Type:application/json"})

	reqjson = json.loads(request.body.decode("utf-8"))

	# TODO: Check for Anonymous user
	if request.user is None:
		return JsonResponse({'Status':'Failed'})

	# TODO: Fail if T_user doesnt exist
	t_user = TechnicalUser.objects.get(user=request.user)

	d = Dataset(name=reqjson['name'], description=reqjson['description'], owner=t_user)
	d.save()

	return JsonResponse({'Status':'Success'})


@csrf_exempt
def insert_dataelement(request):
	if request.content_type != 'application/json':
		return JsonResponse({"Status":403,"Message" :"Forbidden - Only accepts Content-Type:application/json"})
	reqjson = json.loads(request.body.decode("utf-8"))

	# TODO: Check for Anonymous user
	if request.user is None:
		return JsonResponse({'Status': 'Failed'})

	dataset = reqjson['dataset']
	dataset = Dataset.objects.get(name=dataset)

	data = reqjson['data']

	de = Dataelement(parentset=dataset, data=data)
	de.save()

	return JsonResponse({'Status':'Success'})

@csrf_exempt
def get_dataelements(request):
	if request.content_type != 'application/json':
		return JsonResponse({"Status":403,"Message" :"Forbidden - Only accepts Content-Type:application/json"})
	reqjson = json.loads(request.body.decode("utf-8"))

	# TODO: Check for Anonymous user
	if request.user is None:
		return JsonResponse({'Status': 'Failed'})

	dataset = reqjson['dataset']
	dataset = Dataset.objects.get(name=dataset)

	response = {}
	response_list = []

	results = Dataelement.objects.get(parentset=dataset)

	results.to_string()

	for result in results:
		response_list.append(result)

	response['dataelements'] = response_list

	return JsonResponse(response)