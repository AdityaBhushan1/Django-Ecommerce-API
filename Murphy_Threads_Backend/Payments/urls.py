from Utils.Urls import app_urls
from django.urls import path 
from .views import *

app_name = 'payments'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    path('create-cashfree-payment-session/', CashfreeOrder.as_view(), name='create_cashfree_payment_session'),
    path('create-stripe-payment-intent/', StripePaymentIntent.as_view(), name='create_stripe_payment_intent'),
]