from django.db import models
from users.models import Users
from products.models import Products
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    is_variated_product = models.BooleanField(default=False)
    variated_product=models.ForeignKey(ProductsVariations,on_delete=models.CASCADE, null =True)
    quantity = models.PositiveIntegerField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)