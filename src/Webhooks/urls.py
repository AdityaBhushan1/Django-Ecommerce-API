from Utils.Urls import app_urls
from django.urls import path 
from .StirpeViews import *
from .CashFreeViews import *


app_name = 'webhooks'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    path('stripe/payment_intent/', Stripe.payment_intent, name='payment_intent'),
    path('stripe/refund/', Stripe.refund, name='payment_intent'),
]