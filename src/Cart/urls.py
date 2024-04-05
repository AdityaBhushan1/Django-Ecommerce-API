from Utils.Urls import app_urls
from django.urls import path 
from .views import *

app_name = 'Cart'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    path("cart/", CartView.as_view(),name="user_home_page"),
]
