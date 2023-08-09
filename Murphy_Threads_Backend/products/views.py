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
# class ProdductCategoriesView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAdminUser]

#     def patch(self,request,pk):
#         try:
#             category = ProductCategory.objects.get(pk=pk)
#         except ProductCategory.DoesNotExist:
#             return Response({'message':'category does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = ProductCategorySerializer(category, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'message':'successfully updated category'
#                 }, 
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         try:
#             category = ProductCategory.objects.get(pk=pk)
#         except ProductCategory.DoesNotExist:
#             return Response({'message':'category does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
#         category.delete()
#         return Response(
#             {
#                 'message':'successfully deleted the category'
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# class NewProductsCategroyView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAdminUser]
#     def post(self,request):
#         serializer = ProductCategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             formatted_data = {
#             "message": 'successfully added new category'
#             }
#             return Response(formatted_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    


# class ProductView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAdminUser]        
    
#     def patch(self,request,pk):
#         try:
#             product = Products.objects.get(pk=pk)
#         except Products.DoesNotExist:
#             return Response({'message':'product does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = ProductsSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'message':'successfully updated category'
#                 }, 
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         try:
#             product = Products.objects.get(pk=pk)
#         except Products.DoesNotExist:
#             return Response({'message':'product does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
#         product.delete()
#         return Response(
#             {
#                 'message':'successfully deleted the category'
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# class NewProductView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAdminUser]
#     def post(self,request):
#         serializer = ProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             formatted_data = {
#             "message": 'successfully added new product'
#             }
#             return Response(formatted_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListProductByCategoryView(APIView):
    renderer_classes = [UserRenderer]
    def get(self,request,pk):
        category_id = pk
        queryset = Products.objects.filter(category=category_id)
        serializer = ProductsSerializer(queryset, many=True)
        for product in serializer.data:
            product['average_rating'] = Products.objects.get(pk=product['pid']).average_rating()

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
        try:
            serializer_product = ProductsSerializer(product)
        except:
            return Response(serializer_product.errors, status=status.HTTP_400_BAD_REQUEST)
        reviews = Review.objects.filter(product=pk)
        reviews_serializer = ReviewSerializer(reviews, many=True)
        variations = product.generate_variations()

        formatted_data = {
            "data": serializer_product.data,
            "variations":variations,
            "review":reviews_serializer.data
        }
        # if product.generate_variations == True:
        #     queryset = ProductVariations.objects.filter(product=pk)
        #     variations_serializer = ProductVariationsSerializer(queryset, many=True)
        #     formatted_data['variations']=variations_serializer.data
        return Response(formatted_data, status=status.HTTP_200_OK)
    
# class GetProductVariationView(APIView):
#     renderer_classes = [UserRenderer]
#     def get(self,request,pk):
#         product_id = pk
#         queryset = ProductVariations.objects.filter(product=product_id)
#         serializer = ProductVariationsSerializer(queryset, many=True)
#         formatted_data = {
#             "product_id": product_id,
#             "variations": serializer.data
#         }
#         return Response(formatted_data, status=status.HTTP_200_OK)

class ReviewView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request,pk):
        user = request.user
        if Review.objects.filter(user=user, product=pk).exists():
            return Response({"message":"You have already reviewed this product."}, status=status.HTTP_400_BAD_REQUEST)
        request.data['product'] = pk
        request.data['user'] = request.user.id
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            formated_data = {"message":"successfull reviewed the product"}
            return Response(formated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request,pk):
        product_id = pk
        try:
            review = Review.objects.get(user=request.user,product=product_id)
        except review.DoesNotExist:
            return Response({'message':'review does not exsist'}, status=status.HTTP_400_BAD_REQUEST)
        review.delete()
        return Response(
            {
                'message':'successfully deleted the review'
            },
            status=status.HTTP_204_NO_CONTENT
        )
