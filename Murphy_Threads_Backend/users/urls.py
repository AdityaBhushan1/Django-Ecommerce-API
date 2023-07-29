from utils.urls import app_urls
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView
from django.contrib import admin 
from django.urls import path, include 
from .views import *

app_name = 'users'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/',UserRegistrationView.as_view(),name="register"),
    
    # path('get-user-by-username/<str:username>', views.get_user_by_username, name='get_user_by_username'),

    #  path('get_user_addresses/<str:username>',views.get_user_addresses,name="get_user_addresses"),

    
    #  path("update-user/<str:username>",views.update_user,name="update_user"),
    
    #  path('delete-user/<str:username>',views.delete_user,name="delete_user"),
    
    #  path("account/verify/<str:username>/<str:email_token>",views.activate_account,name="account_activation"),

    #  path('request-password-reset/<str:username>',views.request_password_reset,name="pass_reset_request"),

    #  path('password-reset/<str:pass_reset_token>',views.reset_pass,name="pass_reset"),

    #  path('add-address/',views.add_new_address,name="add_new_address"),
     
    #  path('update-address/<int:id>',views.update_address,name="address_update"),

    #  path("delete-address/<int:id>",views.delete_address,name="address_delete"),
]