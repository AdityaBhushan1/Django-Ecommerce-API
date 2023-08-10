from django.conf import settings
from utils.renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import *
from cart.models import *
from django.db import transaction

class OrderView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        queryset = Order.objects.filter(user=request.user.id)
        if not queryset:
            return Response({'message':'no orders found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(queryset, many=True)
        formatted_data = {
            "user": request.user.id,
            "orders": serializer.data
        }
        return Response(formatted_data, status=status.HTTP_200_OK)

    def post(self, request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    shipping_address_id = request.data.get('shipping_address')
        
    if not cart_items:
        return Response({'message': 'No items found in cart'}, status=status.HTTP_400_BAD_REQUEST)
        
     shipping_address = UserAddresses.objects.get(id=shipping_address_id)
        
    try:
         with transaction.atomic():
         order = Order.objects.create(
             user=user,
                    shipping_address_id=shipping_address_id,
                    ammount_paid=request.data.get('ammount')
                )
                
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                        product=cart_item.product,
                        size=cart_item.size,
                        color=cart_item.color,
                        quantity=cart_item.quantity
                    )
                
            cart_items.delete()
            
        return Response(
                {
                    'message': 'Successfully created order',
                    'order_id': order.id
                },
                status=status.HTTP_200_OK
            )
    except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SpecificOrderView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            order_queryset = Order.objects.get(pk=pk)
        except:
            return Response({'message':'no order found'},status=status.HTTP_400_BAD_REQUEST)
        order_serializer = OrderSerializer(order_queryset)
        queryset = Order.objects.filter(user=request.user.id)
        serializer = OrderItemSerializer(queryset, many=True)
        formatted_data = {
            "order_details": order_serializer.data,
            "Items": serializer.data
        }
        return Response(formatted_data, status=status.HTTP_200_OK)

    # def patch(self,request,pk):
    #     ...

