
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("murphy-threads-admin-panel/", admin.site.urls),
    path('', views.home, name='home'),
    path("users/", include("Users.urls"),name = 'user'),
    # path("cart/", include("cart.urls"),name = 'cart'),
    # # path("extra/", include("extra.urls"),name = 'extra'),
    # path("order/", include("orders.urls"),name = 'order'),
    # path("payment/", include("payments.urls"),name = 'payment'),
    # path("products/", include("products.urls"),name = 'products'),
    # path("wishlist/", include("wishlist.urls"),name = 'wishlist'),

]
