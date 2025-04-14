from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}

    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    
    # if instance:
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price
    #     # data = model_to_dict(instance, fields=['id', 'price', 'sale_price','title'])
    #     data = ProductSerializer(instance).data
        
        # data = dict(data)
        #json_data_str = json.dumps(data)
        # response = HttpResponse(data, content_type="application/json")
        # print(response['content-type'])
    # return HttpResponse(data, content_type="application/json")
