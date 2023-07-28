from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .manager import UserManager

# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):      
    email = models.EmailField(primary_key=True,max_length=255,null=False,unique=True)
    # password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    phone_no = models.CharField(null=False,max_length=13)
    country_code = models.CharField(max_length=255, default=None,null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255,null = True,unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_no']

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_staff
    
    @is_staff.setter
    def is_staff(self, value = False):
        self._is_staff = value
        self.save()



class UserAddresses(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='email')
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

