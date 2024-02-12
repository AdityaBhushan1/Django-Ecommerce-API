from django.db import models
from Products.models import Products
from Users.models import Users

# Create your models here.
class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
