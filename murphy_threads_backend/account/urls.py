from django.contrib import admin 
from django.urls import path, include 
from .views import *
  
 urlpatterns = [ 
     path("", account_index,name="user_home_page"), 
     path('/get-user-by-username/<str:username>', get_user_by_username, name='get_user_by_username'),
path("/get-user-by-id/<int:user_id>",get_user_by_id,name="get_user_by_id"),
path('get_user_addresses/<int:user_id>',get_user_addresses,name="get_user_addresses"),
]