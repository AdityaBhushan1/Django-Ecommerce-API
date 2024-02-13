from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from Users.models import *
from Orders.models import *
from Payments.models import *
from Orders.serializers import *
from Payments.serializers import *

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
            payment_intent = event['data']['object']

            payment_serializer = PaymentSearializer(payments,data = {'status':'CANCELED'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            order.delete()

            return HttpResponse(status = 200)

        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']

            payment_serializer = PaymentSearializer(payments,data = {'status':'REJECTED'})

            if payment_serializer.is_valid():
                payment_serializer.save()

            order.delete()

            return HttpResponse(status = 200)

        elif event['type'] == 'payment_intent.processing':
            payment_intent = event['data']['object']

            payment_serializer = PaymentSearializer(payments,data = {'status':'PROCESSING'})

            if payment_serializer.is_valid():
                payment_serializer.save()
                
            return HttpResponse(status = 200)

        elif event['type'] == 'payment_intent.requires_action':
            payment_intent = event['data']['object']

        elif event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']

            order_serializer = OrderSerializer(order, data={'status':'CONFIRMED'}, partial=True)

            if order_serializer.is_valid():
                order_serializer.save()

            payment_serializer = PaymentSearializer(payments,data = {'status':'PAID'})

            if payment_serializer.is_valid():
                payment_serializer.save()

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

        order = Order.objects.get(pk=event['data']['object']['meta_data']['order_id'])

        user = Users.objects.get(email = event['data']['object']['receipt_email']) #Todo change 'recipt_email' to correct email present in event data

        payments = Payments.objects.get(payment_id = event['data']['object']['id']) #Todo change 'id' to payment id in event data

        # Handle the event
        if event['type'] == 'refund.created':
            refund = event['data']['object']

        refund = Refunds.objects.get(refund_id = event) #Todo add path to refund_id provided by stripe in event data
        if event['type'] == 'refund.updated':
            refund = event['data']['object']
            # ... handle other event types
        else:
            print('Unhandled event type {}'.format(event['type']))

            return HttpResponse(status=200)
