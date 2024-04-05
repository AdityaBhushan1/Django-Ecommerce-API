from django.db import models
from Utils.AutoField import CustomAutoField as AutoField
from Users.models import *
from Orders.models import *

class Shipping(models.Model):
    id = AutoField(prefix= "ship_",primary_key=True)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    dispatched_date = models.DateField(null = True)
    shipped_date = models.DateField(null = True)
    delivered_date = models.DateField(null = True)
    shipment_id = models.DateField(max_length = 1000)
    awb = models.DateField(max_length = 1000)
    shipping_partner = models.CharField(max_length=1000)
    crated_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)