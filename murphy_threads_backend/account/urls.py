from django.contrib import admin 
from django.urls import path, include 
from .views import *
  
 urlpatterns = [ 
     path("", account_index,name="user_home_page"), 
     path('/get-user-by-username/<str:username>', get_user_by_username, name='get_user_by_username'),
path("/get-user-by-id/<int:pk>",get_user_by_id,name="get_user_by_id"),
path('/get_user_addresses/<int:uid>',get_user_addresses,name="get_user_addresses"),
path('/create-user/',create_new_user,name="create_new_user"),
path("/update-user/<int:pk>",update_user,name="update_user"),
path('/delete-user/<int:id>',delete_user,name="delete_user"),
]