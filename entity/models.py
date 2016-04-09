from django.db import models
from source_data.models import City,Area,Street,Category,SubCategory

# Create your models here.
class business_entity(models.Model):
    
    name = models.CharField(max_length=200,blank=True);
    profile = models.CharField(max_length=4096,blank=True,null=True);
    services = models.CharField(max_length=4096,blank=True,null=True);
    timings = models.CharField(max_length=150,blank=True,null=True);
    contact_person = models.CharField(max_length=150,blank=True,null=True);
    address = models.CharField(max_length=1000,blank=True,null=True);
    mobile = models.CharField(max_length=10,blank=True,null=True);
    whatsapp = models.CharField(max_length=10,blank=True,null=True)
    Email = models.EmailField(max_length=70,blank=True,null=True)
    website = models.CharField(max_length=70,blank=True,null=True)
    social_media = models.CharField(max_length=300,blank=True,null=True)
    customer_rating = models.FloatField(blank=True,null=True,)
    city = models.ForeignKey(City,blank=True,null=True)
    area = models.ForeignKey(Area,blank=True,null=True)
    locality = models.ForeignKey(Street,blank=True,null=True)
    category = models.ForeignKey(Category,blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory,blank=True,null=True)
    
    def __str__(self):
    	return self.name
