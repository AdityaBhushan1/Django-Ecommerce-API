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
            elif data['type'] == 'PAYMENT_USER_DROPPED_WEBHOOK':
                ...
            
        except Exception as e:
            return HttpResponse(status = 400)
        
    @csrf_exempt
    def refunds(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
            if data['type'] == 'REFUND_STATUS_WEBHOOK':
                ...
            elif data['type'] == 'AUTO_REFUND_STATUS_WEBHOOK':
                ...
            
        except Exception as e:
            return HttpResponse(status = 400)
        
    @csrf_exempt
    def settlements(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
            if data['type'] == 'SETTLEMENT_INITIATED':
                ...
            elif data['type'] == 'SETTLEMENT_SUCCESS':
                ...
            elif data['type'] == 'SETTLEMENT_FAILED':
                ...
            elif data['type'] == 'SETTLEMENT_REVERSED':
                ...
            
        except Exception as e:
            return HttpResponse(status = 400)
        
    @csrf_exempt
    def disputes(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
            if data['type'] == 'DISPUTE_CREATED':
                ...
            elif data['type'] == 'DISPUTE_UPDATED':
                ...
            elif data['type'] == 'DISPUTE_CLOSED':
                ...
            
        except Exception as e:
            return HttpResponse(status = 400)
