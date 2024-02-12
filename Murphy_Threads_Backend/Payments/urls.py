from Utils.Urls import app_urls
from django.urls import path 
from .views import *

app_name = 'payments'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    # path('create-payment-session/', CreatePaymentSession.as_view(), name='create_payment_session'),
]