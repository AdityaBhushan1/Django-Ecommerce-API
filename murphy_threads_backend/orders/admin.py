from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Orders)
admin.site.register(OrderState)
admin.site.register(Refunds)
admin.site.register(Returns)