from Utils.Renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from Payments.Stripe.StripeHandler import createRefund as StripeRefund
from Payments.models import Payments


class RequestCancellationView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        order = Order.object.get(id=request.data.get("order_id"))
        pay = Payments.objects.get(order=order.id)

        try:
            cancellation = Cancellation.objects.create(
                user=user, order=order, reason=request.data.get("reason")
            )

            if order.payment_mode == "ONLINE":
                if pay.payment_menthod == "STRIPE":
                    StripeRefund(
                        payid=pay.payment_id,
                        ammount=request.data.get("ammount"),
                        oid=order.id,
                        uid=user.id,
                    )
                elif pay.payment_menthod == "PAYPAL":
                    ...  # Todo create paypal refund

                elif pay.payment_menthod == "INSTAMOJO":
                    ...  # Todo create instamojo refund

            cancellation.update(status="CANCELLED")
            return Response(
                {
                    "message": "Successfully Cancelled Order, Refund Money Will Be Refunded To Your Payment Source In 5 To 10 Bussiness Days",
                    "cancellation_id": cancellation.id,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# class UpdateCancellationView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAuthenticated or IsAdminUser]

#     def patch(self,request,pk):
#         order = Order.objects.get(id=pk)

#         try:
#             cancellation = Cancellation.objects.get(order=order.id)
#         except UserAddresses.DoesNotExist:
#             return Response({'message':'Cancellation Request does not exsist'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = Cancellation(cancellation, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()

#             # order.update(status = request.data.get("status"))

#             if request.data.get("CANCELLATION_APPROVED") == "CANCELLATION_APPROVED":
#                 # create a refund
#                 order.update(status = "CANCELLED")


#             return Response(
#                 {
#                     'message':'successfully updated Cancellation Request'
#                 },
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
