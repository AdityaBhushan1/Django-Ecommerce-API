from django.db import models
from Users.models import *
from Orders.models import *
from Utils.AutoField import CustomAutoField as AutoField

PAYMENT_METHOD_CHOICES = (
    ("PAYPAL", "Paypal"),
    ("STRIPE", "Stripe"),
    ("INSTAMOJO", "Instamojo"),
    ("CASHFREE", "Cashfree"),
)

PAYMENT_STATUS = (
    ("PENDING", "Pending"),
    ("PROCESSING", "Processing"),
    ("PAID", "Paid"),
    ("REQUESTED_REFUND", "Requested Refund"),
    ("REFUNDED_INITIATED", "Refunded Initiated"),
    ("REFUNDED", "Refunded"),
    ("REFUND_REJECTED", "Refund Rejected"),
    ("CANCELED", "Canceled"),
    ("REJECTED", "Rejected"),
)

REFUND_STATUS = (
    ("REQUESTED_REFUND", "Requestedrefund"),
    ("REFUNDED_INITIATED", "Refundedinitiated"),
    ("REFUNDED", "Refunded"),
    ("REFUND_REJECTED", "Refundrejected"),
)

SETTLEMENTS_STATUS = (
    ("INITIATED", "Initiated"),
    ("SUCCESS", "Success"),
    ("FAILED", "Failed"),
    ("REVERSED", "Reversed"),
)


class Payments(models.Model):
    id = AutoField(prefix="pay_", primary_key=True)
    payment_menthod = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=500)
    payment_id = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    ammount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.CharField(choices=PAYMENT_STATUS, default="PENDING")
    rejection_reason = models.CharField(max_legth=999)
    paid_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Refunds(models.Model):
    id = AutoField(prefix="ref_", primary_key=True)
    refund_id = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ammount_to_refund = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.CharField(choices=REFUND_STATUS, default="REQUESTED_REFUND")
    refund_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Settlements(models.Model):
    id = AutoField(prefix="settle_", primary_key=True)
    settlement_id = models.CharField(null=True)
    amount_settled = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    payment_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.CharField(choices=SETTLEMENTS_STATUS)
    settlement_type = models.CharField(null=True)
    settled_on = models.DateTimeField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
