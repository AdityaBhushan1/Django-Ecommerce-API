from Utils.Urls import app_urls
from django.urls import path 
from .views import *

app_name = 'Cashfree'

urlpatterns = [ 
    path('create-cashfree-payment-session/', CashfreeOrder.as_view(), name='create_cashfree_payment_session'),
]