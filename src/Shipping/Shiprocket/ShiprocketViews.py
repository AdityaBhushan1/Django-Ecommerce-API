from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Users.models import *
from Orders.models import *
from Payments.models import *
from Orders.serializers import *
from Payments.serializers import *
from Utils.DiscordWebhooks import send_discord_message as SendDiscordWebhook
from Shipping.models import *

@csrf_exempt
def shiprocket_view(request):
    if request.method == "POST":
        shiprocket_webhook_key = request.headers.get('x-api-key')
        if shiprocket_webhook_key == settings.SHIPROCKET_WEBHOOK_KEY:
            payload = request.body
            # order = Order.objects.get(id = payload['order_id'])
            shipping = Shipping.objects.get(order = payload['order_id'])

            if payload['shipment_status_id'] == 1:
                shipping.update(awb = payload['awb'])
                # Todo send user email with shipping details like tracking number and links
                return HttpResponse(status=200)
            
            elif payload['shipment_status_id'] == 2:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 3:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 4:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 5:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 6:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 7:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 8:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 9:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 10:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 11:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 12:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 13:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 14:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 15:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 16:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 17:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 18:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 19:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 20:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 21:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 22:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 23:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 24:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 25:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 26:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 38:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 39:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 40:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 41:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 42:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 43:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 44:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 45:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 46:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 47:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 48:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 49:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 50:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 51:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 52:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 53:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 54:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 55:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 56:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 57:
                return HttpResponse(status=200)

            elif payload['shipment_status_id'] == 59:
                return HttpResponse(status=200)

            else:
                print(f'Unhandled status type {payload['shipment_status_id']} : {payload['shipment_status']}') #Todo Convert This to discord webhooks
                return HttpResponse(status=200)