from django.conf import settings
from .ShiprocketWrapper import ShiprocketWrapper as ShipRocket

Shiprocket = ShipRocket(settings.SHIPROCKET_API_KEY)
