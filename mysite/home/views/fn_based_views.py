from django.http import JsonResponse
import json

def get_logs(request):
    res = {
        "success": True,
        "message": "Function based view: api to get logs"
    
    }
    return JsonResponse(res)

def create_logs(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        res = {
            "success": True,
            "message": "Function based view: api to create a log"
    }
    else:
        res = {
            "success": False,
            "message": "Function based view: Invalid request"
        }
    return JsonResponse(res)

def update_logs(request):
    if request.method == 'PUT':
        res = {
            "success": True,
            "message": "Function based view: api to update a log"
    }
    else:
        res = {
            "success": False,
            "message": "Function based view: Invalid request"
        }
    return JsonResponse(res)