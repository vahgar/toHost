from django.shortcuts import render, HttpResponse
from source_data.forms import CityForm,AreaForm,LocationForm,CategoryForm
# Create your views here.
def checkselect(request):
	form_x = LocationForm();
	form_y = CategoryForm();
	context = {'form':form_x, 'form1':form_y}
	return render(request,'result.html',context);
