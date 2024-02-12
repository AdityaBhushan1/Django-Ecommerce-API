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
from .StripeHandler import *

# class CreatePaymentSession(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAuthenticated]


#     def post(self,request):
#         price = request.data.get('price')
#         return_url = f'{settings.SITE_DOMAIN}/{request.data.get('return_path')}'
#         redirection_url = f'{settings.SITE_DOMAIN}/{request.data.get('redirect_path')}'
#         cart_id = request.data.get("cart_id")
#         email = request.data.get("user_email")
#         expires_at = request.data.get("expiry")

#         session = create_checkout_session(
#             price = price,
#             return_url = return_url,
#             success_url = redirection_url,
#             card_id = cart_id,
#             user = request.user.id,
#             email = email,
#             expiry = expires_at,
#         )

#         return Response(
#                 {
#                     'message': 'Successfully created payment session',
#                     'session_id': session
#                 },
#                 status=status.HTTP_200_OK
#             )