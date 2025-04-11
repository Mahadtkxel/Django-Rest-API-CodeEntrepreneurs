from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from products.models import Product




def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}

    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data, fields=['id', 'price','title'])
    return JsonResponse(data)    
        # data = dict(data)
        #json_data_str = json.dumps(data)
        # response = HttpResponse(data, content_type="application/json")
        # print(response['content-type'])
    # return HttpResponse(data, content_type="application/json")
