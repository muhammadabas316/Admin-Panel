
from django.db import models
from django.db.models import ImageField
# Create your models here.

TAGS= (('corolla','corolla'),('hilux','hilux'),)

class spare_part(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/spare")
    vehicle = models.CharField(choices=TAGS, max_length=100, default='hilux')
    description = models.TextField()
    in_stock= models.BooleanField(default=True)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=100)
    price = models.IntegerField()


    def __str__(self):
        return self.name
    
