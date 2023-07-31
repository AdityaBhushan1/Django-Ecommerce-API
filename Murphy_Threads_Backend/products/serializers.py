from rest_framework import serializers 
from .models import * 


class ProductCategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ProductCategory
        fields = "__all__"

        extra_kwargs = { 
            'desc': {'required': False},
            'is_parent_category': {'required': False},
            'is_child_category': {'required': False}
        }

