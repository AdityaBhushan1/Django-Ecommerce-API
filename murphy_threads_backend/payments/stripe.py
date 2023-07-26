import stripe
from django.conf import settings


if settings.DEBUG == True:
    stripe.api_key = settings.STRIPE_LIVE_KEY
else:
    stripe.api_key = settings.STRIPE_TEST_KEY