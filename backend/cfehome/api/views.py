from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # request is not same as python library requests
    # request -> HttpRequest (class)-> Django
    print(request.GET)
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers # old -> request.META ->
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
