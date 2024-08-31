
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("murphy-threads-admin-panel/", admin.site.urls),
    path('', views.home, name='home'),
    path("users/", include("Users.urls"),name = 'user'),
    # path("cart/", include("Cart.urls"),name = 'cart'),
    # # path("extra/", include("Extra.urls"),name = 'extra'),
    # path("order/", include("Orders.urls"),name = 'order'),
    # path("products/", include("Products.urls"),name = 'products'),
    # path("wishlist/", include("Wishlist.urls"),name = 'wishlist'),
    # path("payments/", include("Payments.urls"),name = 'payments'),
    # path("webhooks/", include("Webhooks.urls"),name = 'webhooks'),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),

]
