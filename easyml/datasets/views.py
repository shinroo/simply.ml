# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from easyml.util.http_helpers import ok, invalid_request_only_accept_json, require_authenticated_user, get_technical_user
from label.models import Label
from users.models import TechnicalUser


@csrf_exempt
def new_dataset(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return require_authenticated_user()

    t_user = get_technical_user(request.user)

    d = Dataset(name=reqjson['name'], description=reqjson['description'], owner=t_user)
    d.save()

    return ok()


@csrf_exempt
def insert_dataelement_into_dataset(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return require_authenticated_user()

    dataset_name = reqjson['dataset']
    #TODO: check that user is owner of dataset!
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    if dataset.owner.user != request.user:
        return JsonResponse({'status': 403, 'message': 'Forbidden - You are not the owner of this dataset'})
    data = reqjson['data']

    de = DataElement(parentset=dataset, data=data)
    de.save()

    return ok()


@csrf_exempt
def insert_labelchoice_into_dataset(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return require_authenticated_user()

    dataset_name = reqjson['dataset']
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})
    if dataset.owner.user != request.user:
        return JsonResponse({'status': 403, 'message': 'Forbidden: you are not the owner of this dataset'})
    labelname = reqjson['name']
    de = LabelChoice(parentset=dataset, name=labelname)
    de.save()

    return ok()