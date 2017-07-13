# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
import json

from users.models import TechnicalUser

@csrf_exempt
def create_technical_user(request):
	if request.content_type != 'application/json':
		return JsonResponse({"status": 400, "message": "Invalid Request - Only accepts Content-Type:application/json"})

	reqjson = json.loads(request.body.decode("utf-8"))
	try:
		validate_password(reqjson['password'])
	except Exception as e:
		return JsonResponse({'Status': 400, "Message":str(e)})

	# TODO: Verify Email etc...
	try:
		user = User.objects.create_user(reqjson['username'], reqjson['email'], reqjson['password'])
	except IntegrityError as e:
		return JsonResponse({'status': 400, "message" : "Username already taken"})

	user.save()
	t = TechnicalUser(user=user)
	t.save()
	return JsonResponse({'status' : 200, 'message' : 'OK'})
