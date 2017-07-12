# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
import json

from users.models import TechnicalUser

@csrf_exempt
def create_technical_user(request):
	if request.content_type != 'application/json':
		return JsonResponse({"Status":403,"Message" :"Forbidden - Only accepts Content-Type:application/json"})

	reqjson = json.loads(request.body.decode("utf-8"))
	try:
		validate_password(reqjson['password'])
	except Exception as e:
		return JsonResponse({'Status':str(e)})

	user = User.objects.create_user(reqjson['username'], reqjson['email'], reqjson['password'])
	user.save()
	t = TechnicalUser(user=user)
	t.save()
	return JsonResponse({'Status':'Success'})
