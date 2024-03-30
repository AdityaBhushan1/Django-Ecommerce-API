from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cashfree_pg.api_client import Cashfree
from Users.models import *
from Orders.models import *
from Payments.models import *
from Orders.serializers import *
from Payments.serializers import *
from Utils.DiscordWebhooks import send_discord_message as SendDiscordWebhook

class Cashfree:
    @csrf_exempt
    def payment_session(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
            if data['type'] == 'PAYMENT_SUCCESS_WEBHOOK':
                ...
            elif data['type'] == 'PAYMENT_FAILED_WEBHOOK':
                ...
            
        except Exception as e:
            return HttpResponse(status = 400)
