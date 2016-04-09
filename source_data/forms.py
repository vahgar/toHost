from django.forms import ModelForm
from source_data.models import City,Area,Street,Locality,ChooseCategory

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name']

class AreaForm(ModelForm):
	class Meta:
		model = Area
		fields = ['name','city']

class LocationForm(ModelForm):
	class Meta:
		model = Locality
		fields = ['city','area','street'] 

class CategoryForm(ModelForm):
	class Meta:
		model = ChooseCategory
		fields = ['category','subCategory']