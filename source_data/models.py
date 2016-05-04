from django.db import models
from smart_selects.db_fields import ChainedForeignKey 

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Area(models.Model):
	city = models.ForeignKey(City)
	name = models.CharField(max_length=255)
	

	def __str__(self):
		return self.name

class Street(models.Model):
	area = models.ForeignKey(Area)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Locality(models.Model):
	
	city = models.ForeignKey(City,related_name="cityofloc")
	area = ChainedForeignKey(
		Area,
		chained_field="city",
		chained_model_field="city",
		show_all=False,
		auto_choose=False,
		)
	street = ChainedForeignKey(
		Street,
		chained_field="area",
		chained_model_field="area",
		show_all=False,
		auto_choose=False,

		)

	def __str__(self):
		return self.street.name

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255,blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
    	return self.name

class SubsubCategory(models.Model):
	name = models.CharField(max_length=255,blank=True,null=True)
	subCategory = models.ForeignKey(SubCategory)

	def __str__(self):
		return self.name

class ChooseCategory(models.Model):
	category = models.ForeignKey(Category)
	subCategory = ChainedForeignKey(
		SubCategory,
		chained_field="category",
		chained_model_field="category",
		show_all=False,
		auto_choose=False,
		)

	subsubCategory = ChainedForeignKey(
		SubsubCategory,
		chained_field="subCategory",
		chained_model_field="subCategory",
		show_all=False,
		auto_choose=False,
		blank=True,
		null=True,
		)



	def __str__(self):
		return self.name	

