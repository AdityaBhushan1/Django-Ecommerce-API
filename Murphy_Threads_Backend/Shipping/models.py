from django.db import models
from Utils.AutoField import CustomAutoField as AutoField
from Users.models import *
from Orders.models import *

SHIPPING_PARTNER_CHOICE = (
    ("DELHIVERY","delhivery"),
    ("DTDC","dtdc"),
    ("EKART","ekart"),
    ("BLUEDART","bluedart"),
    ("AMAZON","amazon"),
    ("SHADOWFX","shadowfx"),
    ("XPRESSBEES","xpressbees"),
    ("ARAMEX_INTERNATIONAL","aramex international"),
    ("KERY_INDEV","kery indev"),
)

# Create your models here.
class Shipping(models.Model):
    id = AutoField(prefix= "ship_",primary_key=True)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    dispatched_date = models.DateField(null = True)
    shipped_date = models.DateField(null = True)
    delivered_date = models.DateField(null = True)
    consignment_id = models.DateField(max_length = 1000)
    shipping_partner = models.CharField(choices=SHIPPING_PARTNER_CHOICE, max_length=1000)
    crated_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)