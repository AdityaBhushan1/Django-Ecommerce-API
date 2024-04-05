from Utils.Urls import app_urls
from django.urls import path 
from .views import *

app_name = 'products'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),  
    path("get-categories/<pk>/", GetCategroyView.as_view(),name="get-categories"), 
    path("get-product/<pk>/", GetProductView.as_view(),name="get-product"), 
    path("list-products-by-categories/<pk>/", ListProductByCategoryView.as_view(),name="list-products-by-categories"), 
    path("review/<pk>/", ReviewView.as_view(),name="review"), 
]
