from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
from django.db.models import Avg
from Users.models import Users
from Utils.AutoField import CustomAutoField as AutoField

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(primary_key = True,max_length=255,null=False,unique = True)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=500,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_parent_category = models.BooleanField(null=True)
    is_child_category = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField(max_length=50,primary_key = True)
    size_nickname = models.CharField(max_length=256,null = True)

    def __str__(self):
        return self.size_nickname

class Color(models.Model):
    color_in_hex = models.CharField(max_length=256,primary_key = True)
    color_nickname = models.CharField(max_length=256,null = True)

    def __str__(self):
        return self.color_nickname

class Products(models.Model):
    id = AutoField(prefix= "prod_",primary_key=True,null = False,unique=True)
    name = models.CharField(max_length=255,null=False)
    slug = models.SlugField(unique=True)
    short_desc = models.CharField(max_length=500,null=False)
    long_desc = models.CharField(max_length=5000,null=False)
    main_price = models.DecimalField(decimal_places = 2,max_digits = 20,null = False)
    sale_price = models.DecimalField(decimal_places = 2,max_digits = 20,null = True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    SKU = models.CharField(max_length=255,null=False)
    main_image = models.URLField(null = True)
    gallery_image = ArrayField(models.URLField(),null = True)
    colors = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    is_available = models.BooleanField(default = True)
    # generate_variations = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def average_rating(self):
        reviews = Review.objects.filter(product=self)
        total_reviews = reviews.count()
        if total_reviews > 0:
            average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            average_rating = round(average_rating, 1)
        else:
            average_rating = 0
        return average_rating

    # def generate_variations(self):
    #     variations = []
    #     for color in self.colors:
    #         for size in self.sizes:
    #             variations.append({"color": color, "size": size})
    #     return variations



# class ProductVariations(models.Model):
#     id = models.AutoField(primary_key=True,null = False,unique=True)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     size = models.ForeignKey(Size, on_delete=models.CASCADE)
#     color = models.ForeignKey(Color, on_delete=models.CASCADE)
#     price_addition = models.DecimalField(decimal_places = 2,max_digits = 20,null = True,default = 00.00)
#     is_available = models.BooleanField(default = True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.product.name} - {self.color.color_nickname} - {self.size.size_nickname}"

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(max_length=900,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
