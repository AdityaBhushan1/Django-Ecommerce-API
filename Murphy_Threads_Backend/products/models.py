from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
import re
from django.core.validators import RegexValidator

COLOR_VALIDATOR = RegexValidator(r'^#(?:[0-9a-fA-F]{3}){1,2}$', 'only valid hex color code is accepted')

# Create your models here.
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True,null = False)
    name = models.CharField(max_length=255,null=False)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=500,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_parent_category = models.BooleanField(null=True)
    is_child_category = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Size(models.Model):
    size = models.CharField(max_length=50)
    size_nickname = models.CharField(max_length=256,default='add nickname',null = True)

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    color_in_hex = models.CharField(max_length=256, validators=[COLOR_VALIDATOR], default='#000000')
    color_nickname = models.CharField(max_length=256,default='add nickname',null = True)

    def __str__(self):
        return self.color_nickname

class Products(models.Model):
    pid = models.AutoField(primary_key=True,null = False,unique=True)
    name = models.CharField(max_length=255,null=False)
    slug = models.SlugField(unique=True)
    short_desc = models.CharField(max_length=500,null=False)
    long_desc = models.CharField(max_length=5000,null=False)
    main_price = models.DecimalField(decimal_places = 2,max_digits = 20,null = False)
    sale_price = models.DecimalField(decimal_places = 2,max_digits = 20,null = True)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, to_field='id',null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    SKU = models.CharField(max_length=255,null=False)
    main_image = models.URLField(null = True)
    gallery_image = ArrayField(models.URLField(),null = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Inventory(models.Model):
    id = models.AutoField(primary_key=True,null = False,unique=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE,to_field='pid',null = False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    quantity_availabel = models.IntegerField(default=10)
    sale_price = models.DecimalField(decimal_places = 2,max_digits = 20,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
