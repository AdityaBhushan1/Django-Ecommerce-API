from django.conf import settings
from Utils.Renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..serializers import *
from rest_framework.permissions import IsAuthenticated
from ..models import *
from Cart.models import *
from Utils.ErrorHandler import StripeErrors as handlestripe
from ..Cashfree import CashFreeHandler as cashfree

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