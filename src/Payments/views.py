from django.conf import settings
from Utils.Renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import *
from Cart.models import *
from django.db import transaction
from . import StripeHandler as stripe
from Utils.ErrorHandler import StripeErrors as handlestripe
from . import CashFreeHandler as cashfree

class StripePaymentIntent(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    @handlestripe
    def post(self,request):
        try:
            customer = stripe.createCustomer(
                email = request.user.email,
                name = request.user.name
            )

            intent = stripe.createPaymentIntent(
                email = customer.email,
                cid = customer.id,
                oid = request.data.get("oid"),
                amount = request.data.get("amount"),
                mid = (
                    request.data.get('mid') if request.data.get('mid') != None else None
                ),
                save_method = (
                    True if request.data.get("save_method") != False else False
                )
            )
        except Exception as e:
            return Response({'error':e}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(
            {
                'client_secret':intent
            },
            status=status.HTTP_201_CREATED
        )

class CashfreeOrder(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self,request):

        try:
            order = cashfree.CreateOrder(
                oid = request.data.get("oid"),
                amount = request.data.get("amount"),
                customer = request.user
            )

        except Exception as e:
            return Response({'error':e}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(
            {
                'session':order
            },
            status=status.HTTP_201_CREATED
        )