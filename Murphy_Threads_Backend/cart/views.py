from django.shortcuts import render
from django.conf import settings
from utils.renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import *
# Create your views here.

class CartView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            user_id = request.user.id
            try:
                queryset = Cart.objects.filter(user=user_id)
            except:
                return Response({'message':'no items in cart'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = CartSerializer(queryset, many=True)
            formatted_data = {
                "user_id": user_id,
                "Cart_Item's": serializer.data
            }
            return Response(formatted_data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = request.user
            product = request.data.get('product')
            quantity = int(request.data.get('quantity'))
            try:
                cart_item = Cart.objects.get(user=user, product_id=product)
                cart_item.quantity += quantity
                cart_item.save()
            except Cart.DoesNotExist:
                request.data['user'] = request.user.id
                serializer = CartSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'message':'successfuly added item to cart'}, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            user = request.user
            product = request.data.get('product')
            quantity = int(request.data.get('quantity'))
            action = request.data.get('action')

            try:
                cart_item = Cart.objects.get(user=user, product_id=product)

                if action == 'add':
                    cart_item.quantity += quantity
                elif action == 'deduct':
                    remaining_quantity = cart_item.quantity - quantity

                    if remaining_quantity <= 0:
                        cart_item.delete()
                        return Response({'message':'cart updated successfully'}, status=status.HTTP_200_OK)
                    cart_item.quantity = remaining_quantity
                else:
                    return Response({"error": "Invalid action provided. Use 'add' or 'deduct'."}, status=status.HTTP_400_BAD_REQUEST)

                cart_item.save()

                serializer = CartSerializer(cart_item)
                return Response({'message':'cart updated successfully'}, status=status.HTTP_200_OK)

            except Cart.DoesNotExist:
                return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        product_id = request.data.get('product')

        try:
            cart_item = Cart.objects.get(user=user, product_id=product_id)
            cart_item.delete()

            return Response({"message": "Cart item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)
