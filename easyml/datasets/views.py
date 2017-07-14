# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from easyml.util.http_helpers import ok, invalid_request_only_accept_json, require_authenticated_user, get_technical_user
from datasets.models import Dataset, DataElement, LabelChoice


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
def get_datasets(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    if not request.user.is_authenticated():
        return require_authenticated_user()

    # TODO: Only display datasets that user has permission to see!
    datasets = Dataset.objects.all()
    # .filter("HAS PERMSSION")

    return JsonResponse({"datasets": [dataset.toDict() for dataset in datasets]})


@csrf_exempt
def get_labelchoices(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return require_authenticated_user()

    dataset_name = reqjson['dataset']
    # TODO: check that user has permission to see dataset!
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    labelchoices = LabelChoice.objects.filter(parentset=dataset)

    return JsonResponse({"labelchoices": [choice.toDict() for choice in labelchoices]})


@csrf_exempt
def insert_dataelement_into_dataset(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return require_authenticated_user()

    dataset_name = reqjson['dataset']
    # TODO: check that user is owner of dataset!
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist:
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
    except ObjectDoesNotExist:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})
    if dataset.owner.user != request.user:
        return JsonResponse({'status': 403, 'message': 'Forbidden: you are not the owner of this dataset'})
    labelname = reqjson['name']
    # TODO: error handling on already existing labelchoice!
    de = LabelChoice(parentset=dataset, name=labelname)
    de.save()

    return ok()
