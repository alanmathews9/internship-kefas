from django.views.generic import View
from django.http import JsonResponse

class LogsView(View):
    def get(self, request):
        res = {
        "success": True,
        "message": "Class based view: api to get logs"
    
        }
        return JsonResponse(res)
    
    def post(self, request, *args, **kwargs):
        res = {
        "success": True,
        "message": "Class based view: api to create logs"
    
        }
        return JsonResponse(res)
    
    def put(self, request, *args, **kwargs):
        res = {
        "success": True,
        "message": "Class based view: api to update logs"
    
        }
        return JsonResponse(res)
    
    def delete(self, request, *args, **kwargs):
        res = {
        "success": True,
        "message": "Class based view: api to delete logs"
    
        }
        return JsonResponse(res)