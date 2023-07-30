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
    # path('account/activate/<str:uid>/<str:token>/', ActivateView.as_view(), name='activate'),
    path('activate/', ActivationConfirm.as_view(), name='activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('delete/', DeleteAccountView.as_view(), name='user_delete'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('email-update/', UserEmailUpdateView.as_view(), name='email-update'),
    path('phone-no-update/', UserPhoneNoUpdateView.as_view(), name='email-update'),

    
    #  path('get_user_addresses/<str:username>',views.get_user_addresses,name="get_user_addresses"),

    
    #  path("update-user/<str:username>",views.update_user,name="update_user"),

    #  path('add-address/',views.add_new_address,name="add_new_address"),

    #  path('update-address/<int:id>',views.update_address,name="address_update"),

    #  path("delete-address/<int:id>",views.delete_address,name="address_delete"),
]