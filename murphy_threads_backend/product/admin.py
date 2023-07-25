from django.contrib import admin
from product.models import *

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductImages)
admin.site.register(ProductCategory)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Inventory)