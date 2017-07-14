from django.http import JsonResponse

def invalid_request_only_accept_json():
    return JsonResponse({"status": 400, "message": "Invalid Request - Only accepts Content-Type:application/json"})

def require_authenticated_user():
    return JsonResponse({'status': 403, "message": "Forbidden - Only available to authenticated users!"})

def ok():
    return JsonResponse({'status': 200, 'message': 'OK'})