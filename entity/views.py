from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import Http404
from .models import business_entity
from django.core import serializers
import json

class error():
	def out(self):
		print("works")
# Create your views here.
def mobileapi(request):
	data = business_entity.objects.all();
	data_list = []
	for i in data:
		data_list.append({'NAME':i.name,'CONTACT_PERSON':i.contact_person,'SERVICES':i.services,'SOCIAL_MEDIA':i.social_media,'CATEGORY':i.category.name,'WHATSAPP':i.whatsapp,'LOCALITY':i.locality.name,'WEBSITE':i.website,'AREA':i.area.name,'MOBILE':i.mobile,'EMAIL':i.Email,'TIMINGS':i.timings,'CITY':i.city.name,'SUBCATEGORY':i.subcategory.name,'PROFILE':i.profile,'CUSTOMER_RATING':i.customer_rating,'ADDRESS':i.address,'SUBSUBCATEGORY':i.subsubcategory.name,'image_1':'/media/'+i.image_1.name,'image_2':'/media/'+i.image_2.name,'image_3':'/media/'+i.image_3.name})
	data_list_json =json.dumps(data_list,indent=4)
	return HttpResponse(data_list_json,content_type="application/json")


def details(request,entity_name):
	entity = get_object_or_404(business_entity, name=entity_name)
	data = business_entity.objects.get(id=entity.id)
	image_list = []
	if(entity.image_1):
		image_list.append(entity.image_1.url)
	if(entity.image_2):
		image_list.append(entity.image_2.url)
	if(entity.image_3):
		image_list.append(entity.image_3.url)
	context = {"entity": data, "image_list":image_list}
	return render(request,'images.html',context);
