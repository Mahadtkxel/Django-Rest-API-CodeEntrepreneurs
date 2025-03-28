from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # request is not same as python library requests
    # request -> HttpRequest (class)-> Django
    
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python dict
    except:
        pass
    print(data.keys())
    return JsonResponse(data)
