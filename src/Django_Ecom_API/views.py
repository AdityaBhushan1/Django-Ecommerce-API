from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from django.db import connections
from django.db.utils import OperationalError

@api_view(["GET"])
def home(request):
    data = {
        "name": "Django E-Commerce API",
        "version": "1.0.0",
        "status": "online",
        "schema": "/api/schema/",
        "docs": "/api/docs/",
        "redoc": "/api/redoc/",
        "health": "/api/health/",
    }
    return Response(data)


@api_view(["GET"])
def health(request):
    db_status = "disconnected"

    try:
        connections["default"].cursor()
        db_status = "connected"
    except OperationalError:
        db_status = "disconnected"

    data = {
        "status": "ok" if db_status == "connected" else "degraded",
        "database": db_status,
    }

    return Response(data)


# Specify an empty list for permission_classes to remove the default permissions
# home.permission_classes = []
home.permission_classes = [AllowAny]
