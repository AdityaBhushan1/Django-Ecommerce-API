from Utils.Renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from Payments.Stripe.StripeHandler import createRefund as StripeRefund
from Payments.models import Payments
from Utils.DiscordWebhooks import send_discord_message as DiscordWebhook


class RequestReturnView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        order = Order.object.get(id = request.data.get("order_id"))
        pay = Payments.objects.get(order = order.id)

        try:
            returns = Return.objects.create(
                    user=user,
                    order=order,
                    reason = request.data.get("reason")
                )
            order.update(status = "RETURN_REQUESTED")

            DiscordWebhook(
                webhook_url=settings.DISCORD_RETURN_LOGS,
                title = "Return",
                desciption="Return Requested",
                fields = [
                    {
                        'name':'Return ID:',
                        'value':returns.id,

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
                        'name':'Amount:',
                        'value':pay.ammount,
                    },
                    {
                        'name':'Status:',
                        'value':'Return Requested',
                    },
                ]
            )

            # Todo send email to user with instructions to verify return request

            return Response(
                {
                    'message': 'Successfully Created Return Request, Request will be updated in 2 to 3 bussiness days and you will recive an email with further instrunctions.',
                    'return_id': returns.id
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)