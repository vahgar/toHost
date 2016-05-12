from django.shortcuts import render,HttpResponse
from .models import business_entity
from django.core import serializers
import json
# Create your views here.
def mobileapi(request):
	data = business_entity.objects.all();
	data_list = []
	for i in data:
		data_list.append({'NAME':i.name,'CONTACT_PERSON':i.contact_person,'SERVICES':i.services,'SOCIAL_MEDIA':i.social_media,'CATEGORY':i.category.name,'WHATSAPP':i.whatsapp,'LOCALITY':i.locality.name,'WEBSITE':i.website,'AREA':i.area.name,'MOBILE':i.mobile,'EMAIL':i.Email,'TIMINGS':i.timings,'CITY':i.city.name,'SUBCATEGORY':i.subcategory.name,'PROFILE':i.profile,'CUSTOMER_RATING':i.customer_rating,'ADDRESS':i.address,'SUBSUBCATEGORY':i.subsubcategory.name,'image_1':'/media/'+i.image_1.name,'image_2':'/media/'+i.image_2.name,'image_3':'/media/'+i.image_3.name})
	data_list_json =json.dumps(data_list,indent=4)	
	return HttpResponse(data_list_json,content_type="application/json")
