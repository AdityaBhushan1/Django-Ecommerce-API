from django.shortcuts import render
from utils.renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAdminUser
from django.conf import settings
from .models import *

# Create your views here.
class ProdductCategoriesView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]

    def patch(self,request,pk):
        try:
            category = ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return Response({'message':'category does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'successfully updated category'
                }, 
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            category = ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return Response({'message':'category does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        category.delete()
        return Response(
            {
                'message':'successfully deleted the category'
            },
            status=status.HTTP_204_NO_CONTENT
        )

class NewProductsCategroyView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]
    def post(self,request):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            formatted_data = {
            "message": 'successfully added new category'
            }
            return Response(formatted_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetCategroyView(APIView):
    renderer_classes = [UserRenderer]
    def get(self,request,pk):
        try:
            category = ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return Response({'message':'category does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductCategorySerializer(category)
        formatted_data = {
            "data": serializer.data
        }
        return Response(formatted_data, status=status.HTTP_200_OK)
    


class ProductView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]        
    
    def patch(self,request,pk):
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({'message':'product does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'successfully updated category'
                }, 
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({'message':'product does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        return Response(
            {
                'message':'successfully deleted the category'
            },
            status=status.HTTP_204_NO_CONTENT
        )

class NewProductView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]
    def post(self,request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            formatted_data = {
            "message": 'successfully added new product'
            }
            return Response(formatted_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListProductByCategoryView(APIView):
    renderer_classes = [UserRenderer]
    def get(self,request,pk):
        category_id = pk
        queryset = Products.objects.filter(category_id=category_id)
        serializer = ProductsSerializer(queryset, many=True)
        formatted_data = {
            "category": category_id,
            "products": serializer.data
        }
        return Response(formatted_data, status=status.HTTP_200_OK)
    
class GetProductView(APIView):
    renderer_classes = [UserRenderer]
    def get(self,request,pk):
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({'message':'product does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductsSerializer(product)
        formatted_data = {
            "data": serializer.data
        }
        return Response(formatted_data, status=status.HTTP_200_OK)
