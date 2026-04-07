from rest_framework import serializers
from .models import *


class PaymentSearializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

        extra_kwargs = {"rejection_reason": {"required": False}}


class RefundSearializer(serializers.ModelSerializer):
    class Meta:
        model = Refunds
        fields = "__all__"
