from Utils.Urls import app_urls
from django.urls import path 
from .views import *

app_name = 'wishlist'

urlpatterns = [ 
    path("", app_urls,{'app_name': app_name},name="user_home_page"),
    path("wish/",WishlistView.as_view(),name="wishlist"),
    path("wish-delete/<pk>/",DeleteWishlistView.as_view(),name="wishlist-delete")

]
