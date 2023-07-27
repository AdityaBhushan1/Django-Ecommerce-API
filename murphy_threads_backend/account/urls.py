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
     path("/account/verify/<str:username>/<int:pk>/<str:email_token>",activate_account,name="account_activation"),
     path('/request-password-reset/<int:pk>',request_password_reset,name="pass_reset_request"),
     path('/password-reset/<str:pass_reset_token>,reset_pass,name="pass_reset"),
     path('/add-address/<int:id>',add_new_address,name="add_new_address"),
     path('/update-address/<int:id>',update_address,name="address_update"),
path("/delete-address/<int:id>",delete_address,name="address_delete"),
]