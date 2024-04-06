from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from Users.models import *
from Orders.models import *
from Payments.models import *
from Orders.serializers import *
from Payments.serializers import *
from Utils.DiscordWebhooks import send_discord_message as SendDiscordWebhook

class Stripe:
# ******************************Payment Webhooks*******************************#
    @csrf_exempt
    def payment_intent(request):
        payload = request.body
        event = None
        sig_header = request.headers['STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )

        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)
        
        order = Order.objects.get(pk=event['data']['object']['meta_data']['order_id'])

        user = Users.objects.get(email = event['data']['object']['receipt_email'])


        if event['type'] == 'payment_intent.created':
            payment_intent = event['data']['object']

            Payments.objects.create(
                    payment_method=u"STRIPE",
                    order=order.id,
                    user=user.id,
                    ammount = payment_intent['amount'],
                    status = "PENDING"
                )
            
            return HttpResponse(status=200)
        
        payments = Payments.objects.get(payment_id = event['data']['object']['id'])
        
        if event['type'] == 'payment_intent.canceled':
            # payment_intent = event['data']['object']

            payment_serializer = PaymentSearializer(payments,data = {'status':'CANCELED'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            order.delete()

            return HttpResponse(status = 200)

        elif event['type'] == 'payment_intent.payment_failed':
            # payment_intent = event['data']['object']

            payment_serializer = PaymentSearializer(payments,data = {'status':'REJECTED'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            order.delete()

            return HttpResponse(status = 200)

        elif event['type'] == 'payment_intent.processing':
            # payment_intent = event['data']['object']

            payment_serializer = PaymentSearializer(payments,data = {'status':'PROCESSING'})

            if payment_serializer.is_valid():
                payment_serializer.save()
                
            return HttpResponse(status = 200)

        elif event['type'] == 'payment_intent.requires_action':
            payment_intent = event['data']['object']
            SendDiscordWebhook(
                webhook_url=settings.DISCORD_STRIPE_PAYMENT,
            )


        elif event['type'] == 'payment_intent.succeeded':
            # payment_intent = event['data']['object']

            order_serializer = OrderSerializer(order, data={'status':'CONFIRMED'}, partial=True)

            # OrderStatus.objects.filter(order=order.id).update()

            if order_serializer.is_valid():
                order_serializer.save()

            payment_serializer = PaymentSearializer(payments,data = {'status':'PAID'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            SendDiscordWebhook(
                webhook_url=settings.DISCORD_STRIPE_PAYMENT,
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


        else:
            print('Unhandled event type {}'.format(event['type']))

            return HttpResponse(status=200)

# ******************************Refund Webhooks*******************************#
    @csrf_exempt
    def refund(request):
        payload = request.body
        event = None
        sig_header = request.headers['STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )

        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        order = Order.objects.get(pk=event['data']['object']['metadata']['order_id'])
        user = Users.objects.get(id = event['data']['object']['metadata']['user_id'])
        payments = Payments.objects.get(payment_id = event['data']['object']['payment_intent'])

        # Handle the event
        if event['type'] == 'refund.created':
            refund = event['data']['object']
            refunds = Refunds.objects.create(
                refund_id = refund['id'],
                user = user.id,
                payment = payments.id,
                order = order.id,
                ammount_to_refund = refund['amount'],
                status = "REFUND_INITIATED"
            )

            payments.update(status = "REFUNDED_INITIATED")
            Order.update(status = "REFUNDED_INITIATED")

            SendDiscordWebhook(
                webhook_url=settings.DISCORD_STRIPE_REFUND,
                title = "Refund",
                desciption="Refund Created",
                fields = [
                    {
                        'name':'Refund ID:',
                        'value':refunds.id,

                    },
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
                        'value':refund['amount'],
                    },
                    {
                        'name':'Status',
                        'value':'Refund Initialized',
                    },
                ]
            )

            return HttpResponse(status=200)

        refund = Refunds.objects.get(refund_id = event['data']['object']['id']) 
        if event['type'] == 'refund.updated':
            refund = event['data']['object']

            if refund['status'] == 'failed':
                SendDiscordWebhook(
                webhook_url=settings.DISCORD_STRIPE_REFUND,
                title = "Refund",
                desciption="Refund Failed",
                fields = [
                    {
                        'name':'Refund ID:',
                        'value':refunds.id,

                    },
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
                        'value':refund['amount'],
                    },
                    {
                        'name':'Status',
                        'value':'Refund Failed',
                    },
                    {
                        'name':'Reason',
                        'value':refund['failure_reason'],
                    },
                ]
            )
            payments.update(status = "REFUND_REJECTED")
            order.update(status = "REFUND_REJECTED")
            refund.update(status = "REFUND_REJECTED")
            # Todo inform user about refund failiure using email and tell them about further process

        elif event['type'] == 'charge.refunded':
            charge = event['data']['object']
            payments.update(status = "REFUNDED")
            order.update(status = "REFUNDED")
            refund.update(status = "REFUNDED",refund_date = ...)#Todo set date of refund
            SendDiscordWebhook(
                webhook_url=settings.DISCORD_STRIPE_REFUND,
                title = "Refund",
                desciption="Refunded",
                fields = [
                    {
                        'name':'Refund ID:',
                        'value':refunds.id,

                    },
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
                        'value':refund['amount'],
                    },
                    {
                        'name':'Status',
                        'value':'Refund Done',
                    },
                ]
            )
            # Todo inform user about refund through email


        else:
            print('Unhandled event type {}'.format(event['type']))

            return HttpResponse(status=200)
