from utils.urls import app_urls
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView
from django.contrib import admin 
from django.urls import path, include 
from .views import *

app_name = 'cart'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"), 
]