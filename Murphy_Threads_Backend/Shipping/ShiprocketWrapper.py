import requests
import json
from Utils.GetCurrentDateTime import get_current_datetime
from django.conf import settings
from Users.models import *
from Orders.models import *

class ShiprocketWrapper:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://apiv2.shiprocket.in/v1/external'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

    def CreateOrder(self,oid,user,baddrid,saddrid,paymenttype,price):
        url = self.base_url + '/orders/create/adhoc'

        b_usr_addr = UserAddresses.objects.get(id = baddrid)
        order_item = OrderItem.objects.filter(order = oid)

        order_items = []

        for item in order_item:
            item_data = {
                "name": item.product.name,
                "sku": item.product.sku,
                "units": item.quantity,
                "selling_price": item.product.sale_price,
                }
            
        order_items.append(item_data)
        
        payload = {
            "order_id": oid,
            "order_date": get_current_datetime(),
            "pickup_location": settings.SHIPROCKET_PICKUP_LOCATION,
            "channel_id": settings.SHIPROCKET_CHANNEL_ID,
            "billing_customer_name": user.name,
            "billing_address": b_usr_addr.address_line_1,
            "billing_address_2": b_usr_addr.address_line_2,
            "billing_city": b_usr_addr.city,
            "billing_pincode": b_usr_addr.postal_code,
            "billing_state": b_usr_addr.state,
            "billing_country": b_usr_addr.country,
            "billing_email": b_usr_addr.email,
            "billing_phone": b_usr_addr.phone_no_1,
            "order_items": order_items,
            "payment_method": "Prepaid" if paymenttype == "ONLINE" else "COD",
            "sub_total": price,
            "length": settings.PACKAGE_LENGTH,
            "breadth": settings.PACKAGE_BREADTH,
            "height": settings.PACKAGE_HEIGHT,
            "weight": settings.PACKAGE_WEIGHT
        }

        if baddrid != saddrid:
            s_usr_addr = UserAddresses.objects.get(id = saddrid) 

            payload.update({
                "shipping_is_billing": False,
                "shipping_customer_name": s_usr_addr.name,
                "shipping_address": s_usr_addr.address_line_1,
                "shipping_address_2": s_usr_addr.address_line_2,
                "shipping_city": s_usr_addr.city,
                "shipping_pincode": s_usr_addr.postal_code,
                "shipping_country": s_usr_addr.country,
                "shipping_state": s_usr_addr.state,
                "shipping_email": s_usr_addr.email,
                "shipping_phone": s_usr_addr.phone_no_1,
            })
        else:
            payload["shipping_is_billing"] = True

        payload_json = json.dumps(payload)
        response = requests.request("POST", url, headers=self.headers, data=payload_json)

        return response.json()
    
    

