from rest_framework import serializers 
from .models import * 


class CategorySerializer(serializers.ModelSerializer): 
     class Meta: 
         model = ProductCategory
         fields = "__all__"
  
         extra_kwargs = { 
             'desc': {'required': False}
         }