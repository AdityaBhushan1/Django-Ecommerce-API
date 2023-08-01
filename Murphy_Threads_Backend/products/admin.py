from django.contrib import admin
from .models import *

class ProductCategoryAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "id",
        "name",
        "slug",
        "desc",
        "is_parent_category",
        "is_child_category"
        )
    
class SizeAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "size",
        "size_nickname"
        )
    
class ProductColorAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "color_in_hex",
        "color_nickname"
        )
    
class ProductsAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "pid",
        "name",
        "slug",
        "short_desc",
        "long_desc",
        "main_price",
        "sale_price",
        "category_id",
        "SKU",
        "main_image",
        "gallery_image",
        "default_color",
        "default_size",
        "is_available",
        )

class ProductVariationsAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "id",
        "product",
        "size",
        "color",
        "price_addition",
        "is_available",
        )

# Register your models here.
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductVariations, ProductVariationsAdmin)
admin.site.register(ProductColor, ProductColorAdmin)