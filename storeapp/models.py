from django.db import models

# Create your models here.
class Item(models.Model):
    product = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images',default='Image')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    
    def __str__(self):
        return self.product