from django.contrib import admin
from source_data.models import City,Area,Locality,Street,Category,ChooseCategory,SubCategory,SubsubCategory
# Register your models here.
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Locality)
admin.site.register(Street)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ChooseCategory)
admin.site.register(SubsubCategory)

