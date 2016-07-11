from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import Http404
from .models import ads_image
from django.core import serializers
import json

# This place is for views

def adimages(request):
    data = ads_image.objects.all()
    data_list = []
    for i in data:
        data_list.append({"Name":i.name,"URL_NAME":i.images.name})
    data_list_json =json.dumps(data_list,indent=4)
    return HttpResponse(data_list_json,content_type="application/json")
