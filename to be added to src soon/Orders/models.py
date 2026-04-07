from django.db import models
from Users.models import *
from Products.models import *
from Utils.AutoField import CustomAutoField as AutoField

ORDER_STATUS_CHOICES = (
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("PROCESSING", "Processing"),
    ("DISPATCHED", "Dispatched"),
    ("SHIPPED", "Shipped"),
    ("DELIVERED", "Delivered"),
    # ('CANCELLATION_REQUESTED', 'Cancellation Requested'),
    # ('CANCELLATION_APPROVED', 'Cancellation Approved'),
    ("CANCELLED", "Cancelled"),
    ("RETURN_REQUESTED", "return_requested"),
    ("RETURN_APPROVED", "return_approved"),
    ("RETURN_REJECTED", "return_rejected"),
    ("RETURING", "Returning"),
    ("RETURNED", "Returned"),
    # ("REQUESTED_REFUND","Requestedrefund"),
    ("REFUNDED_INITIATED", "Refundedinitiated"),
    ("REFUNDED", "Refunded"),
    ("REFUND_REJECTED", "Refundrejected"),
)

PAYMENT_MODE = (("ONLINE", "Online"), ("COD", "Cash On Delivery"))

CANCELLATION_STATUS = (
    # ('CANCELLATION_REQUESTED', 'Cancellation Requested'),
    # ('CANCELLATION_APPROVED', 'Cancellation Approved'),
    ("CANCELLED", "Cancelled"),
)

RETURN_STATUS = (
    ("RETURN_REQUESTED", "return_requested"),
    ("RETURN_APPROVED", "return_approved"),
    ("RETURN_REJECTED", "return_rejected"),
    ("RETURING", "Returning"),
    ("RETURNED", "Returned"),
)


class Order(models.Model):
    id = AutoField(prefix="ord_", primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    shipping_address_id = models.ForeignKey(UserAddresses, on_delete=models.CASCADE)
    status = models.CharField(
        choices=ORDER_STATUS_CHOICES, default="PENDING", max_length=1000
    )
    payment_mode = models.CharField(
        choices=PAYMENT_MODE, default="ONLINE", max_length=1000
    )
    status_message = models.CharField(max_length=500, null=True)
    ammount_paid = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    shipping_charges = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    gateway_charges = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    ordered_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


# class OrderStatus(models.Model):
#     id = models.AutoField(primary_key = True)
#     order = models.ForeignKey(Order,on_delete = models.CASCADE)
#     is_pending = models.BooleanField(default = True)
#     is_confirmed = models.BooleanField()
#     is_processing = models.BooleanField()
#     is_processing = models.BooleanField()
#     is_dispatched = models.BooleanField()
#     is_shiped = models.BooleanField()
#     is_delivered = models.BooleanField()
#     cancellation_requested = models.BooleanField()
#     cancellation_approved = models.BooleanField()
#     is_cancelled = models.BooleanField()
#     is_cancelled = models.BooleanField()
#     return_requested = models.BooleanField()
#     is_returning = models.BooleanField()
#     is_returned = models.BooleanField()
#     refund_requested = models.BooleanField()
#     refund_requested = models.BooleanField()
#     refund_initiated = models.BooleanField()
#     is_refunded = models.BooleanField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.order.user


class Cancellation(models.Model):
    id = AutoField(prefix="can_", primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reason = models.TextField(max_length=500)
    status = models.CharField(choices=CANCELLATION_STATUS, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class Return(models.Model):
    id = AutoField(prefix="ret_", primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reason = models.TextField(max_length=500)
    status = models.CharField(
        choices=RETURN_STATUS, default="RETURN_REQUESTED", max_length=1000
    )
    return_recived_date = models.DateField()
    consignment_id = models.CharField(max_lenght=1000)
    return_charges = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
