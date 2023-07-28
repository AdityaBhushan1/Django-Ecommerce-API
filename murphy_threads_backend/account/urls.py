from django.contrib import admin 
from django.urls import path, include 
from . import views
from utils.urls import app_urls

app_name = 'account'

urlpatterns = [ 
     path("", app_urls,{'app_name': app_name},name="user_home_page"), 

     path('get-user-by-username/<str:username>', views.get_user_by_username, name='get_user_by_username'),

     path("get-user-by-id/<int:pk>",views.get_user_by_id,name="get_user_by_id"),

     path('get_user_addresses/<int:uid>',views.get_user_addresses,name="get_user_addresses"),

     path('create-user/',views.create_new_user,name="create_new_user"),
     
     path("update-user/<int:pk>",views.update_user,name="update_user"),
     
     path('delete-user/<int:id>',views.delete_user,name="delete_user"),
     
     path("account/verify/<str:username>/<int:pk>/<str:email_token>",views.activate_account,name="account_activation"),

     path('request-password-reset/<int:pk>',views.request_password_reset,name="pass_reset_request"),

     path('password-reset/<str:pass_reset_token>',views.reset_pass,name="pass_reset"),

     path('add-address/<int:id>',views.add_new_address,name="add_new_address"),
     
     path('update-address/<int:id>',views.update_address,name="address_update"),

     path("delete-address/<int:id>",views.delete_address,name="address_delete"),
     ]