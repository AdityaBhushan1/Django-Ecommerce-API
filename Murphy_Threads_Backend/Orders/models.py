from django.db import models
from Users.models import *
from Products.models import *

ORDER_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('CONFIRMED','Confirmed'),
    ('PROCESSING', 'Processing'),
    ('DISPATCHED', 'Dispatched'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLATION_REQUESTED', 'Cancellation Requested'),
    ('CANCELLATION_APPROVED', 'Cancellation Approved'),
    ('CANCELLATION_DECLINED', 'Cancellation Declined'),
    ('CANCELLED', 'Cancelled'),
    ('RETURING','Returning'),
    ('RETURNED','Returned'),
    ('REFUNDED','Refunded'),
)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    shipping_address_id = models.ForeignKey(UserAddresses, on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='PENDING', max_length=1000)
    status_message = models.CharField(max_length = 500,null = True)
    ammount_paid = models.DecimalField(max_digits = 20,decimal_places = 2,null = True)
    shipped_date = models.DateTimeField(null = True)
    delivered_date = models.DateTimeField(null = True)
    ordered_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return self.order.user

# class Return(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     reason = models.TextField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Cancellation(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     reason = models.TextField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)
