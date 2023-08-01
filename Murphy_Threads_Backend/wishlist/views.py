from django.shortcuts import render
from utils.renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import *


class DeleteWishlistView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def delete(self,request,pk):
        try:
            Wishlist = Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            return Response({'message':'Wish does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        Wishlist.delete()
        return Response(
            {
                'message':'Wish deleted the category'
            },
            status=status.HTTP_204_NO_CONTENT
        )

class WishlistView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user_id = request.user.id
        queryset = Wishlist.objects.filter(user=user_id)
        serializer = WishlistSerializer(queryset, many=True)
        formatted_data = {
            "user_id": user_id,
            "wishlist's": serializer.data
        }
        return Response(formatted_data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            formatted_data = {
            "message": 'successfully added new wish'
            }
            return Response(formatted_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)