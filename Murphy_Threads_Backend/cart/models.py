from django.db import models
from users.models import Users
from products.models import *
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    size = models.CharField(max_length=55,null = True)
    color = models.CharField(max_length=55,null = True)
    quantity = models.PositiveIntegerField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)