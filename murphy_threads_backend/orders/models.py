from django.db import models
from product.models import *
from account.models import *
from django.contrib.auth import get_user_model

Users = get_user_model()

# Create your models here.

class Payments(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',null=False)

class Orders(models.Model):
    orderid = models.AutoField(primary_key=True,null=False)
    usernamr = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',null=False)
    productid = models.ForeignKey(Products, on_delete=models.CASCADE,to_field='pid',null=False)
    shipping_address_id = models.ForeignKey(UserAddresses, on_delete=models.CASCADE,to_field='id')
    ammount_paid = models.DecimalField(max_digits = 20,decimal_places = 2,null = False)
    quantity = models.IntegerField(default = 1,null = False)
    pay_id = models.ForeignKey(Payments, on_delete=models.CASCADE, to_field='id',null=False)
    ordered_on = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    
class OrderState(models.Model):
    id = models.AutoField(primary_key = True,null = False)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, to_field='orderid',null=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid',null=False)
    is_shipped = models.BooleanField(default = False)
    shipped_date = models.DateTimeField(null = True)
    is_delivered = models.BooleanField(default = False)
    delivered_date = models.DateTimeField(null = True)
    is_caceled = models.BooleanField(default = False)
    cancellation_date = models.DateTimeField(null = True)
    cancellation_reason = models.CharField(max_length=500,null = True)
    
class Returns(models.Model):
    id = models.AutoField(primary_key = True,null = False)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, to_field='orderid',null=False)
    username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',null=False)
    is_returned = models.BooleanField(default = False)
    return_applied_date = models.DateTimeField(null = True)
    is_return_applicable = models.BooleanField(default = True)
    return_reason = models.CharField(max_length=500,null = True)


class Refunds(models.Model):
    id = models.AutoField(primary_key = True,null = False)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, 
    to_field='orderid',null=False)
    username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',null=False)
    is_refund_applicable = models.BooleanField(null = True)
    is_refunded = models.BooleanField(null = True)
    refund_date = models.DateTimeField(null = True)
    refund_ammount = models.DecimalField(max_digits = 20,decimal_places = 2,null = True)