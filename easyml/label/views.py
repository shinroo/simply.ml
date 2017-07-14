# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from easyml.util.http_helpers import ok, invalid_request_only_accept_json, require_authenticated_user
from label.models import Dataset, DataElement, LabelChoice, Label
from users.models import TechnicalUser

def get_technical_user(user):
    # TODO: Fail if T_user doesnt exist
    print user.username
    print TechnicalUser.objects.all()
    t_user = TechnicalUser.objects.get(user=user)
    return t_user


@csrf_exempt
def create_dataset(request):
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
def insert_dataelement(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()

    reqjson = json.loads(request.body.decode("utf-8"))

    if not request.user.is_authenticated():
        return require_authenticated_user()
    t_user = get_technical_user(request.user)

    dataset_name = reqjson['dataset']
    #TODO: check that user is owner of dataset!
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 404, "message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    if dataset.owner != t_user:
        return JsonResponse({'status': 403, 'message': 'Forbidden - You are not the owner of this dataset'})
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


@csrf_exempt
def label(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()
    reqjson = json.loads(request.body.decode("utf-8"))
    if not request.user.is_authenticated():
        return require_authenticated_user()

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
        return require_authenticated_user()

    dataset_name = reqjson['dataset']
    #TODO: Check if user has permissions to see the dataset!
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist as e:
        return JsonResponse({'Status': 404, "Message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    response = {}
    response_list = []

    results = DataElement.objects.get(parentset=dataset)

    results.to_string()

    for result in results:
        response_list.append(result)

    response['dataelements'] = response_list

    return JsonResponse(response)

class ShuffledPaginator(Paginator):
    def page(self, number):
        page = super(ShuffledPaginator, self).page(number)
        random.shuffle(page.object_list)
        return page

@csrf_exempt
def get_dataelement_page(request):
    if request.content_type != 'application/json':
        return invalid_request_only_accept_json()
    reqjson = json.loads(request.body.decode("utf-8"))
    if not request.user.is_authenticated():
        return require_authenticated_user()

    dataset_name = reqjson['dataset']
    #TODO: Check if user has permissions to see the dataset!
    try:
        dataset = Dataset.objects.get(name=dataset_name)
    except ObjectDoesNotExist as e:
        return JsonResponse({'Status': 404, "Message": "Not Found - No Dataset with name '" + dataset_name + "' found"})

    paginator = ShuffledPaginator(list(DataElement.objects.filter(parentset=dataset).all()), per_page=5)

    page = reqjson['page']
    #try:
    elements = paginator.page(page)
    #except PageNotAnInteger:
    #    # If page is not an integer, deliver first page.
    #    elements = paginator.page(1)
    #except EmptyPage:
    #    # If page is out of range (e.g. 9999), deliver last page of results.
    #    elements = paginator.page(paginator.num_pages)
    return JsonResponse({"elements":[element.toDict() for element in elements]})