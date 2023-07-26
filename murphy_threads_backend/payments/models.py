from django.db import models
from account.models import Users

# Create your models here.

class SavedCards(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,to_field='uid',null=False)
    card_number = models.BigIntegerField()
    expiry_month = models.IntegerField(null = False)