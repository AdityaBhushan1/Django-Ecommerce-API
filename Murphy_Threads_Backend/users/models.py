from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
# import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from utils.emails import *

class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            name,
            phone_no,
            password=None,
            password2=None
        ):
        if not email:
            raise ValueError("email is required!!!")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_no=phone_no
        )
        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self,email,name,phone_no,password=None):
        user = self.create_user(
            email,
            password=password,
            name = name,
            phone_no=phone_no
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

# Create your models here.
class Users(AbstractBaseUser): 
    id = models.AutoField(primary_key=True)     
    email = models.EmailField(max_length=255,null=False,unique=True)
    # password = models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=False)
    phone_no = models.CharField(null=False,max_length=13)
    country_code = models.CharField(max_length=255, default=None,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_no']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def update_email(self, new_email):
        if Users.objects.filter(email=new_email).exists():
            raise ValidationError("Email already exists.")
        
        self.email = new_email
        self.is_active = False
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        token = default_token_generator.make_token(self)
        activation_url = f'{settings.SITE_DOMAIN}/users/activate/{uid}/{token}'
        send_activation_email(self.email, activation_url)
        self.save()

    def update_phone_no(self, new_phone_no):
        self.phone_no = new_phone_no
        self.save()

    def update_name(self, new_name):
        self.name = new_name
        self.save()


class UserAddresses(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='id')
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null = False)
    address_line_1 = models.CharField(max_length=800,null=False)
    address_line_2 = models.CharField(max_length=800,null=True)
    house_no =  models.CharField(max_length=800,null=True)
    street=  models.CharField(max_length=800,null=True)
    landmark =  models.CharField(max_length=800,null=True)
    state = models.CharField(max_length=255,null=False)
    district = models.CharField(max_length=255,null=False)
    country = models.CharField(max_length=255,null=False)
    postal_code = models.CharField(max_length=255,null=False)
    phone_no_1 = models.CharField(max_length=255,null=False)
    phone_no_2 = models.CharField(max_length=255,null=True)

