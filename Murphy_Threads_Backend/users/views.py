from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from utils.renderers import UserRenderer

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            return Response(
                {
                    'message':'Successfully Registered User!'
                },
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(request,email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(
                {
                    'token':token, 
                    'msg':'Login Success'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'errors':{
                    'non_field_errors':[
                        'Email or Password is not Valid'
                        ]
                    }
                }, 
                status=status.HTTP_404_NOT_FOUND
            )

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
            ) 