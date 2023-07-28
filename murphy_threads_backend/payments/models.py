from django.db import models
from account.models import *

from django.contrib.auth import get_user_model

Users = get_user_model()

# Create your models here.

class SavedCards(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    username = models.ForeignKey(Users,on_delete=models.CASCADE,to_field='username',null=False)
    card_number = models.BigIntegerField()
    expiry_month = models.IntegerField(null = False)