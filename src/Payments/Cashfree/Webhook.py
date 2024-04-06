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
            
            
        except Exception as e:
            return HttpResponse(status = 400)
        
        payments = Payments.objects.get(payment_id = data['data']['payment']['cf_payment_id'])
        order = Order.objects.get(pk=data['data']['order']['order_id'])
        user = Users.objects.get(email = data['data']['customer_details']['customer_id'])

        if data['type'] == 'PAYMENT_SUCCESS_WEBHOOK':
            order_serializer = OrderSerializer(order, data={'status':'CONFIRMED'}, partial=True)

            if order_serializer.is_valid():
                order_serializer.save()

            payment_serializer = PaymentSearializer(payments,data = {'status':'PAID'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            SendDiscordWebhook(
                webhook_url=settings.DISCORD_CASHFREE_PAYMENT,
                title = "Payment",
                desciption="Payment Recived",
                fields = [
                    {
                        'name':'Order ID:',
                        'value':order.id,

                    },
                    {
                        'name':'User Name:',
                        'value':user.name,
                    },
                    {
                        'name':'Amount',
                        'value':payments.ammount,
                    },
                    {
                        'name':'Status',
                        'value':'Paid',
                    },
                ]
            )

            # Todo send email to customer with the bill and telling them we will shortly update them with the tracking link once the order is dispatched
            return HttpResponse(status=200)
        
        elif data['type'] == 'PAYMENT_FAILED_WEBHOOK':
            payment_serializer = PaymentSearializer(payments,data = {'status':'REJECTED'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            order.delete()
            return HttpResponse(status=200)
        
        elif data['type'] == 'PAYMENT_USER_DROPPED_WEBHOOK':
            payment_serializer = PaymentSearializer(payments,data = {'status':'CANCELED'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            order.delete()
            return HttpResponse(status=200)
        
    @csrf_exempt
    def refunds(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
            
        except Exception as e:
            return HttpResponse(status = 400)
        
        payments = Payments.objects.get(payment_id = data['data']['payment']['cf_payment_id'])
        order = Order.objects.get(pk=data['data']['order']['order_id'])
        user = Users.objects.get(email = data['data']['customer_details']['customer_id'])

        if data['type'] == 'REFUND_STATUS_WEBHOOK':
            ...
        elif data['type'] == 'AUTO_REFUND_STATUS_WEBHOOK':
            ...

    @csrf_exempt
    def settlements(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
        except Exception as e:
            return HttpResponse(status = 400)

        if data['type'] == 'SETTLEMENT_INITIATED':
            Settlements.objects.create(
                ammount_settled = data['settlement']['amount_settled'],
                status = data['settlement']['status'],
                settlement_type = data['settlement']['settlement_type'],
                settlement_id = data['settlement']['settlement_id'],
            )
            #Todo set discord webhook
            return HttpResponse(status=200)
        
        settlement = Settlements.objects.get(settlement_id = data['settlement']['settlement_id'])

        if data['type'] == 'SETTLEMENT_SUCCESS':
            settlement.update(status = data['settlement']['status'])
            #Todo set discord webhook
            return HttpResponse(status=200)
        
        elif data['type'] == 'SETTLEMENT_FAILED':
            settlement.update(status = data['settlement']['status'])
            #Todo set discord webhook
            return HttpResponse(status=200)
        
        elif data['type'] == 'SETTLEMENT_REVERSED':
            settlement.update(status = data['settlement']['status'])
            #Todo set discord webhook
            return HttpResponse(status=200)


    @csrf_exempt
    def disputes(request):
        payload = request.body
        timestamp = request.headers['x-webhook-timestamp']
        signature = request.headers['x-webhook-signature']

        try:
            cashfreeWebhookResponse = Cashfree.PGVerifyWebhookSignature(signature, payload, timestamp)
            data = payload['data']
            
        except Exception as e:
            return HttpResponse(status = 400)
        
        payments = Payments.objects.get(payment_id = data['data']['payment']['cf_payment_id'])
        order = Order.objects.get(pk=data['data']['order']['order_id'])
        user = Users.objects.get(email = data['data']['customer_details']['customer_id'])

        if data['type'] == 'DISPUTE_CREATED':
            ...
        elif data['type'] == 'DISPUTE_UPDATED':
            ...
        elif data['type'] == 'DISPUTE_CLOSED':
            ...