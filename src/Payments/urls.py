from Utils.Urls import app_urls
from django.urls import path,include
from .views import *

app_name = 'payments'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    path("stripe/", include("Stripe.urls"),name = 'stripe'),
    path("cashfree/", include("Cashfree.urls"),name = 'cashfree'),
    path("paypal/", include("Papal.urls"),name = 'cashfree'),
]