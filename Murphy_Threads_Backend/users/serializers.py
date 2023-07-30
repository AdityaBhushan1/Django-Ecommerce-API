from rest_framework import serializers
from .models import *
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from utils.emails import send_reset_password_email


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={
            'input_type':'password'
        }, 
        write_only=True
    )

    class Meta:
        model = Users
        fields=[
            'email', 
            'name', 
            'password', 
            'password2',
            'phone_no'
        ]

        extra_kwargs={
            'password':{
                'write_only':True
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self, validate_data):
        return Users.objects.create_user(**validate_data)

    def validate_email(self, value):
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError('user with this Email already exists.')
        return value

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = Users
        fields = [
            'email', 
            'password'
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id', 
            'email', 
            'name',
            'phone_no',
        ]

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, 
        style={
            'input_type':'password'
        }, 
        write_only=True
    )

    password2 = serializers.CharField(
        max_length=255, 
        style={
            'input_type':'password'
        }, 
        write_only=True
    )

    class Meta:
        fields = [
            'password', 
            'password2'
        ]

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:8000/users/reset/'+uid+'/'+token
            # print('Password Reset Link', link)

            # Send EMail
            send_reset_password_email(user.email, link)
            return attrs
        else:
            raise serializers.ValidationError('You are not a Registered User')

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, 
        style={
            'input_type':'password'
        }, 
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, 
        style={
            'input_type':'password'
        }, 
        write_only=True
    )

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = Users.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not Valid or Expired')
