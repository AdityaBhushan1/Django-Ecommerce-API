from django.contrib import admin
from django.urls import path, include
from . import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin-panel/", admin.site.urls),
    path("", views.home, name="home"),
    path("api/health/", views.health, name="health"),
    path("api/users/", include("Users.urls"), name="user"),
    # path("cart/", include("Cart.urls"),name = 'cart'),
    # # path("extra/", include("Extra.urls"),name = 'extra'),
    # path("order/", include("Orders.urls"),name = 'order'),
    # path("products/", include("Products.urls"),name = 'products'),
    # path("wishlist/", include("Wishlist.urls"),name = 'wishlist'),
    # path("payments/", include("Payments.urls"),name = 'payments'),
    # path("webhooks/", include("Webhooks.urls"),name = 'webhooks'),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # OpenAPI schema + docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
