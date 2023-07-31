from utils.urls import app_urls
from django.urls import path 
from .views import *

app_name = 'products'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"), 
    path("categories/<pk>/", ProdductCategoriesView.as_view(),name="categories"), 
    path("categories-new/", NewProductsCategroyView.as_view(),name="categories-new"), 
]