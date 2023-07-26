import stripe
from django.conf import settings


if settings.IS_UNDER_DEVELOPMENT == True:
    stripe.api_key = settings.STRIPE_TEST_KEY
else:
    stripe.api_key = settings.STRIPE_LIVE_KEY