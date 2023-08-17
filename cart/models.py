from django.db import models
from django.contrib.auth.models import User
from services.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)
    quentity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user} => {self.product} => {self.quentity}'
    