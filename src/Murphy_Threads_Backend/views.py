from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


@api_view(["GET"])
def home(request):
    data = {
        "name": "Django E-Commerce API",
        "version": "1.0.0",
        "status": "online",
        "docs": "/api/docs/",
        "redoc": "/api/redoc/",
        "health": "/health/",
    }
    return Response(data)


@api_view(["GET"])
def health(request):
    data = {"status": "ok", "database": "connected"}
    return Response(data)


# Specify an empty list for permission_classes to remove the default permissions
# home.permission_classes = []
home.permission_classes = [AllowAny]
