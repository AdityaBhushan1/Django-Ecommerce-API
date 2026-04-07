from rest_framework import serializers
from .models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

        extra_kwargs = {
            "desc": {"required": False},
            "is_parent_category": {"required": False},
            "is_child_category": {"required": False},
        }


class ProductsSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Products
        fields = "__all__"

        # extra_kwargs = {
        #     'sale_price': {'required': False},
        #     'gallery_image': {'required': False},
        #     'slug': {'required': False},
        # }


# class ProductVariationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductVariations
#         fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

        extra_kwargs = {"comment": {"required": False}}
