from utils.urls import app_urls
from django.urls import path 
from .views import *

app_name = 'orders'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    path("orders/", OrderView.as_view() ,name="order"),
    path("get-specific-order/<pk>/", SpecificOrderView.as_view() ,name="get-specific-order"),
]
