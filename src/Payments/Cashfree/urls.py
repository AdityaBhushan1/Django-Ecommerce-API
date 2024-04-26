from Utils.Urls import app_urls
from django.urls import path 
from .views import *
from .Webhook import *

app_name = 'Cashfree'

urlpatterns = [ 
    path('create-payment/', CashfreeOrder.as_view(), name='create_payment'),
    path('webhook/payment-session/', CashfreeWebhook.payment_session, name='payment-session'),
    path('webhook/payment-session/', CashfreeWebhook.payment_session, name='payment-session'),
    path('webhook/refund/', CashfreeWebhook.payment_session, name='payment-refunds'),
    path('webhook/settlements/', CashfreeWebhook.payment_session, name='settlements'),
    path('webhook/disputes/', CashfreeWebhook.payment_session, name='disputes'),
]