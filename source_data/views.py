from django.shortcuts import render, HttpResponse
from source_data.forms import CityForm,AreaForm,LocationForm,CategoryForm
from .models import City,Area,Street,Category,SubCategory,SubsubCategory
from entity.models import business_entity
from django.db.models import Q
# Create your views here.
def checkselect(request):
	form_x = LocationForm();
	form_y = CategoryForm();
	context = {'form':form_x, 'form1':form_y}
	return render(request,'business_category.html',context);

def index(request):
	return render(request,'index.html')

def icbc(request):
	return render(request,'icbc.html')	


def postandresp(request):
	if request.method == "POST":
		form = LocationForm(request.POST)
		form1 = CategoryForm(request.POST)
		if form.is_valid() and form1.is_valid():
			city = form.cleaned_data['city']
			area = form.cleaned_data['area']
			street = form.cleaned_data['street']
			category = form1.cleaned_data['category']
			subCategory = form1.cleaned_data['subCategory']
			print('Hola1')
			subsubcategory = form1.cleaned_data['Subsubcategory']
			print('Hola')
			data = business_entity.objects.filter(Q(city__name=city),Q(area__name=area),Q(locality__name=street),Q(category__name=category),Q(subcategory__name=subCategory),Q(subsubcategory__name=subsubcategory))
			context = {'data':data}
			return render(request,'display.html',context)
	else:
		form_x = LocationForm();
		form_y = CategoryForm();
		context = {'form':form_x, 'form1':form_y}
		return render(request,'business_category.html',context);