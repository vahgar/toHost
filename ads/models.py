from django.db import models

# Create your models here.
class ads_image(models.Model):
    images = models.ImageField(upload_to = 'ads_image/', blank = True)
    name = models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        if self.name != None:
            return self.name
