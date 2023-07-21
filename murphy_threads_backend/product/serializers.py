from rest_framework import serializers
from product.models import *

# create serailizers here

class Products(serializers.HyperlinkedModelSerializer):
    class Meta:
        models=Products
        feilds = "__all__"

class ProductImage(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = ProductImages
        feilds = "__all__"

class ProductsCategory(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = ProductCategory
        feilds = "__all__"

class ProductsInventory(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Inventory
        feilds = "__all__"
