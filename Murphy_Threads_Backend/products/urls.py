from utils.urls import app_urls
from django.contrib import admin 
from django.urls import path, include 
from .views import *

app_name = 'products'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"), 
]