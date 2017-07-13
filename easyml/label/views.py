# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
import json

from label.models import Dataset, DataElement, LabelChoice, Label
from users.models import TechnicalUser


def invalid_request_only_accept_json():
    return JsonResponse({"status": 400, "message": "Invalid Request - Only accepts Content-Type:application/json"})


def ok():
    return JsonResponse({'status': 200, 'message': 'OK'})


def get_technical_user(user):
    # TODO: Fail if T_user doesnt exist
    t_user = TechnicalUser.objects.get(user=request.user)
    return t_user


@csrf_exempt
def create_dataset(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return JsonResponse({'Status': 403, "Message": "Forbidden - Only available to authenticated users!"})

    t_user = get_technical_user(request.user)

    d = Dataset(name=reqjson['name'], description=reqjson['description'], owner=t_user)
    d.save()

    return ok()


@csrf_exempt
def insert_dataelement(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return JsonResponse({'status': 403, "message": "Forbidden - Only available to authenticated users!"})
    t_user = get_technical_user(request.user)

    dataset_name = reqjson['dataset']

    try:
        dataset = Dataset.objects.get(name=dataset)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    data = reqjson['data']

    de = DataElement(parentset=dataset, data=data)
    de.save()

    return ok()


@csrf_exempt
def insert_labelchoice(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return JsonResponse({'status': 403, "message": "Forbidden - Only available to authenticated users!"})

    dataset_name = reqjson['dataset']
    try:
        dataset = Dataset.objects.get(name=dataset_name, owner=technical_user)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    labelname = reqjson['name']
    de = LabelChoice(parentset=dataset, name=labelname)
    de.save()

    return ok()


@csrf_exempt
def label(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()
    reqjson = json.loads(request.body.decode("utf-8"))
    if not request.user.is_authenticated():
        return JsonResponse({'status': 403, "message": "Forbidden - Only available to authenticated users!"})

    dataset_name = reqjson['dataset']
    try:
        dataset = Dataset.objects.get(name=dataset)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 400, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    element = reqjson['element']
    try:
        dataelement = DataElement.objects.get(parentset=dataset, id=element)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - Invalid DataElement id"})

    label_name = reqjson['label']
    try:
        label = LabelChoice.objects.get(parentset=dataset, name=label_name)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - Invalid Label name"})

    t_user = get_technical_user(request.user)
    new_label = Label.objects.create(user=t_user, labelchoice=label, dataelement=dataelement)
    new_label.save()

    return ok()


@csrf_exempt
def get_dataelements(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return JsonResponse({'Status': 403, "Message": "Forbidden - Only available to authenticated users!"})

    dataset_name = reqjson['dataset']
    try:
        dataset = Dataset.objects.get(name=dataset_name, owner=request.user)
    except ObjectDoesNotExist as e:
        return JsonResponse({'Status': 404, "Message": "Not Found - No Dataset with name '" + dataset_name + "' found"})
    except MultipleObjectsReturned as e:
        print "ERROR - Invalid Database state - two datasets with same name and same owning user!"
        return JsonResponse({'Status': 500, "Message": "Internal Server Error"})

    response = {}
    response_list = []

    results = DataElement.objects.get(parentset=dataset)

    results.to_string()

    for result in results:
        response_list.append(result)

    response['dataelements'] = response_list

    return JsonResponse(response)
