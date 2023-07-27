from django.db import models
from uuid import uuid4
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.description    


def random_file_name_and_path(instance, filename):
    upload_to = 'products'
    ext = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=random_file_name_and_path)

    def __str__(self):
        return f'{self.product} {self.image}'
        
