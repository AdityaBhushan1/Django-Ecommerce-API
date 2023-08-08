from django.db import models
from users.models import Users,UserAddresses
from products.models import *
from cart.models import Cart
from django.db import models

ORDER_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('CONFIRMED','Confirmed'),
    ('PROCESSING', 'Processing'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
    ('RETURING','Returning'),
    ('RETIRNED','Returned'),
    ('REFUNDED','Refunded'),
)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    shipping_address_id = models.ForeignKey(UserAddresses, on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='PENDING', max_length=20)
    status_message = models.CharField(max_length = 500,null = True)
    ammount_paid = models.DecimalField(max_digits = 20,decimal_places = 2,null = True)
    shipped_date = models.DateTimeField(null = True)
    delivered_date = models.DateTimeField(null = True)
    ordered_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class OrderItem():
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delet=models.CASCADE)
    color = models.ForeignKey(Color,on_delet=models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return self.product.name

# class Refund(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     reason = models.TextField(max_length=500)
#     ammount_paid = models.DecimalField(max_digits = 20,decimal_places = 2,null = False)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Return(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     reason = models.TextField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Cancellation(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     reason = models.TextField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)