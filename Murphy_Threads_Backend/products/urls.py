from utils.urls import app_urls
from django.urls import path 
from .views import *

app_name = 'products'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"), 
    # path("categories/<pk>/", ProdductCategoriesView.as_view(),name="categories"), 
    path("get-categories/<pk>/", GetCategroyView.as_view(),name="get-categories"), 
    # path("categories-new/", NewProductsCategroyView.as_view(),name="categories-new"), 
    # path("product/<pk>/", ProductView.as_view(),name="product"), 
    path("get-product/<pk>/", GetProductView.as_view(),name="get-product"), 
    # path("product-new/", NewProductView.as_view(),name="product-new"), 
    path("list-products-by-categories/<pk>/", ListProductByCategoryView.as_view(),name="list-products-by-categories"), 
    path("list-products-variations/<pk>/", GetProductVariationView.as_view(),name="list-products-variations"), 
]