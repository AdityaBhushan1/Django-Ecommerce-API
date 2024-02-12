from django.db import models
from Users.models import *
from Orders.models import *

PAYMENT_CHOICES = (
    ("PAYPAL", "paypal"),
    ("STRIPE", "stripe"),
    ("INSTAMOJO", "instamojo"),
)

class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    payment_menthod = models.CharField(choices=PAYMENT_CHOICES, max_length=500)
    ammount_paid = models.DecimalField(max_digits = 20,decimal_places = 2,null = True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    paid_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class StripeCheckoutSessions(models.Model):
    id = models.CharField(primary_key=True, max_lengths = 200)
    