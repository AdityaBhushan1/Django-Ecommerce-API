from drf_social_oauth2.backends import DjangoOAuth2
from django.urls import reverse

class CustomDjangoOAuth2(DjangoOAuth2):
    AUTHORIZATION_URL = reverse('users:authorize')  # Use 'users' namespace
    ACCESS_TOKEN_URL = reverse('users:token')
    REFRESH_TOKEN_URL = reverse('users:refresh')
