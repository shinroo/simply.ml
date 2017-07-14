from django.http import JsonResponse
from users.models import TechnicalUser

def invalid_request_only_accept_json():
    return JsonResponse({"status": 400, "message": "Invalid Request - Only accepts Content-Type:application/json"})


def require_authenticated_user():
    return JsonResponse({'status': 403, "message": "Forbidden - Only available to authenticated users!"})


def ok():
    return JsonResponse({'status': 200, 'message': 'OK'})

def get_technical_user(user):
    # TODO: Fail if T_user doesnt exist
    t_user = TechnicalUser.objects.get(user=user)
    return t_user
