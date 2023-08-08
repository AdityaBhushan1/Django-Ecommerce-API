from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# class RefundSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Refund
#         fields = '__all__'

# class ReturnSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Return
#         fields = '__all__'

# class CancellationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cancellation
#         fields = '__all__'
