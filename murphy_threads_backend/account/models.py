from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .manager import UserManager

# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):      
    username = models.CharField(primary_key=True,max_length=255,null=False,unique=True)
   # password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,null=False,unique=True)
    phone_no = models.IntegerField(null=False)
    country_code = models.CharField(max_length=255, default=None,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255,null = True,blank = False,unique=True,default=uuid.uuid4())

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','first_name','email','phone_no']
    def __str__(self):
        return self.username


class UserAddresses(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username')
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null = True)
    address_line_1 = models.CharField(max_length=800,null=False)
    address_line_2 = models.CharField(max_length=800,null=True)
    state = models.CharField(max_length=255,null=False)
    district = models.CharField(max_length=255,null=False)
    country = models.CharField(max_length=255,null=False)
    postal_code = models.CharField(max_length=255,null=False)
    phone_no_1 = models.CharField(max_length=255,null=False)
    phone_no_2 = models.CharField(max_length=255,null=True)

