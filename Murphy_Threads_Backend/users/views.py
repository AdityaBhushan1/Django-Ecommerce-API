from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from utils.renderers import UserRenderer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from utils.emails import *
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
# from django.utils.decorators import method_decorator
# from rest_framework.permissions import AllowAny
from django.utils.encoding import force_bytes, force_str

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
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_url = f'{settings.SITE_DOMAIN}/users/activate/{uid}/{token}'
            send_activation_email(user.email, activation_url)
            return Response(
                {
                    'message':'Successfully Registered User!,Successfully Sent The Activation Link'
                },
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

class ActivationConfirm(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        if not uid or not token:
            return Response(
                {
                    'detail': 'Missing uid or token.'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = Users.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                if user.is_active:
                    return Response(
                        {
                            'detail': 'Account is already activated.'
                        }, 
                        status=status.HTTP_200_OK
                    )

                user.is_active = True
                user.save()
                return Response(
                    {
                        'detail': 'Account activated successfully.'
                    }, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'detail': 'Invalid activation link.'
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Users.DoesNotExist:
            return Response(
                {
                    'detail': 'Invalid activation link.'
                }, 
                status=status.HTTP_400_BAD_REQUEST
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

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, 
            context={
                'user':request.user
            }
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                'msg':'Password Changed Successfully'
            }, 
            status=status.HTTP_200_OK
        )
    
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                'msg':'Password Reset link send. Please check your Email'
            }, 
            status=status.HTTP_200_OK
        )

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, 
            context={
                'uid':uid, 
                'token':token
            }
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                'msg':'Password Reset Successfully'
            }, 
            status=status.HTTP_200_OK
        )

class DeleteAccountView(APIView):
    renderer_classes = [UserRenderer]
    def delete(self, request):
        user = request.user
        user.delete()
        logout(request)
        return Response(
            {
                'detail': 'Account deleted successfully.'
            }, 
            status=status.HTTP_204_NO_CONTENT
        )

class UserLogoutView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        logout(request)
        return Response(
            {
                "message": "Logged out successfully"
            }, 
            status=status.HTTP_200_OK
        )
    
class UserEmailUpdateView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request):
        user = request.user

        if 'email' in request.data:
            new_email = request.data['email']
            try:
                user.update_email(new_email)
                return Response(
                    {
                        'message':'user email updated successfully!'
                    },
                    status=status.HTTP_200_OK
                )
            except ValidationError as e:
                return Response(
                    {
                        "error": str(e)
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserPhoneNoUpdateView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request):
        user = request.user

        if 'phone_no' in request.data:
            new_phone_no = request.data['phone_no']
            try:
                user.update_phone_no(new_phone_no)
                return Response(
                    {
                        'message':'user phone no updated successfully!'
                    },
                    status=status.HTTP_200_OK
                )
            except ValidationError as e:
                return Response(
                    {
                        "error": str(e)
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserNameUpdateView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request):
        user = request.user

        if 'name' in request.data:
            new_name = request.data['name']
            try:
                user.update_name(new_name)
                return Response(
                    {
                        'message':'user name updated successfully!'
                    },
                    status=status.HTTP_200_OK
                )
            except ValidationError as e:
                return Response(
                    {
                        "error": str(e)
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
