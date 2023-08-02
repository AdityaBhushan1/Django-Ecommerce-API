from django.contrib import admin
from .models import *
from django import forms

class ProductCategoryAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
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
    
class ColorAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "color_in_hex",
        "color_nickname"
        )
    
# class ProductsAdmin(admin.ModelAdmin):

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserModelAdmin
#     # that reference specific fields on auth.User.
#     list_display = (
#         "pid",
#         "name",
#         "slug",
#         "short_desc",
#         "long_desc",
#         "main_price",
#         "sale_price",
#         "category",
#         "SKU",
#         "main_image",
#         "gallery_image",
#         "default_color",
#         "default_size",
#         "is_available",
#         )

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

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class ProductVariationInline(admin.TabularInline):
    model = ProductVariations

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    filter_horizontal = ('colors',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        if form.instance.generate_variations:
            colors = form.instance.colors.all()
            sizes = Size.objects.all()

            for color in colors:
                for size in sizes:
                    ProductVariations.objects.get_or_create(
                        product=form.instance,
                        color=color,
                        size=size
                    )

    inlines = [ProductVariationInline]

admin.site.register(Products, ProductAdmin)

# Register your models here.
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Size, SizeAdmin)
# admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductVariations, ProductVariationsAdmin)
admin.site.register(Color, ColorAdmin)