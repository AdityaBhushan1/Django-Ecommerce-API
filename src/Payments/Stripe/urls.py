from Utils.Urls import app_urls
from django.urls import path 
from .views import *
from .Webhook import *

app_name = 'Cashfree'

urlpatterns = [ 
    path('create-payment/', PaymentIntent.as_view(), name='create_payment'),
    path('webhook/payment_intent/', Stripe.payment_intent, name='payment_intent'),
    path('webhook/refund/', Stripe.refund, name='payment_intent'),
]