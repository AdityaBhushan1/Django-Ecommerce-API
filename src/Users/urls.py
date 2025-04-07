from Utils.Urls import app_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "users"
app_name = "drf"

urlpatterns = [
    path("", app_urls, {"app_name": app_name}, name="user_home_page"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("is_authenticated/", TokenVerifyView.as_view(), name="is_authenticated"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("activate/", ActivationConfirm.as_view(), name="activate"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path(
        "send-reset-password-email/",
        SendPasswordResetEmailView.as_view(),
        name="send-reset-password-email",
    ),
    path(
        "reset-password/<uid>/<token>/",
        UserPasswordResetView.as_view(),
        name="reset-password",
    ),
    path("delete/", DeleteAccountView.as_view(), name="user_delete"),
    path("logout/", UserLogoutView.as_view(), name="user-logout"),
    path("email-update/", UserEmailUpdateView.as_view(), name="email-update"),
    path("phone-no-update/", UserPhoneNoUpdateView.as_view(), name="phone-no-update"),
    path("name-update/", UserNameUpdateView.as_view(), name="name-update"),
    path("users-addresses/", UserAddressesView.as_view(), name="users-addresses"),
    path(
        "users-addresses/<pk>/",
        UserAddressesUpdateView.as_view(),
        name="users-addresses-update-delete",
    ),
    path(
        "auth/",
        include("drf_social_oauth2.urls", namespace="drf"),
        name="social-oauth2",
    ),
]
