from utils.urls import app_urls
from django.urls import path 
from .views import *

app_name = 'wishlist'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"), 
]