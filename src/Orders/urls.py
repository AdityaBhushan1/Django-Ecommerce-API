from Utils.Urls import app_urls
from django.urls import path
from .OrderViews import *
from .CancellationViews import *
from .ReturnViews import *

app_name = "orders"

urlpatterns = [
    path("", app_urls, {"app_name": app_name}, name="user_home_page"),
    path("orders/", OrderView.as_view(), name="order"),
    path(
        "specific-order/<pk>/", SpecificOrderView.as_view(), name="get-specific-order"
    ),
    # Todo add and test in postman from down there
    path("cancellation/", RequestCancellationView.as_view(), name="cancellation"),
    path("return/", RequestReturnView.as_view(), name="return"),
]
