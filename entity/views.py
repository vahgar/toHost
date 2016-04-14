from django.shortcuts import render,HttpResponse
from .models import business_entity
from django.core import serializers
import json
# Create your views here.
def mobileapi(request):
	data = business_entity.objects.all();
	x = serializers.serialize('json',data,indent=2)
	j_data = json.loads(x)
	return HttpResponse(j_data,content_type="application/json")
