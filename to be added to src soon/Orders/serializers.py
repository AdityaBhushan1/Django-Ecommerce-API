from rest_framework import serializers
from .models import *


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

        extra_kwargs = {"color": {"required": False}, "size": {"required": False}}


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = "__all__"


# class RefundSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Refund
#         fields = '__all__'

# class ReturnSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Return
#         fields = '__all__'


class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = "__all__"


class ReturnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = "__all__"
