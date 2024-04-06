import requests
import json
from Utils.GetCurrentDateTime import *
from django.conf import settings
from Users.models import *
from Orders.models import *
from django.utils import formats

class ShiprocketWrapper:
    def __init__(self, access_token,baseurl):
        self.access_token = access_token
        self.base_url = baseurl
        self.headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

    def CreateOrder(self,oid,baddrid,paymenttype,price,logistic):
        url = self.base_url + f'/order/add.json'

        usr_addr = UserAddresses.objects.get(id = baddrid)
        order_item = OrderItem.objects.filter(order = oid)

        order_items = []

        for item in order_item:
            item_data = {
                "product_name": item.product.name,
                "product_sku": item.product.sku,
                "product_quantity": item.quantity,
                "product_price": item.product.sale_price,
                }
            order_items.append(item_data)

        payload = {
            "data": {
                "shipments": [
                    {
                        "order": oid,
                        "order_date": get_current_date(),
                        "total_amount": price,
                        "name": f"{usr_addr.first_name} {usr_addr.last_name}",
                        "company_name": "ABC Company",
                        "add": usr_addr.address_line_1,
                        "add2": usr_addr.address_line_2,
                        "pin": usr_addr.postal_code,
                        "city": usr_addr.city,
                        "state": usr_addr.state,
                        "country": usr_addr.country,
                        "phone": usr_addr.phone_no_1,
                        "alt_phone": usr_addr.phone_no_2,
                        "email": usr_addr.email,
                        "billing_name": f"{usr_addr.first_name} {usr_addr.last_name}",
                        "billing_add": usr_addr.address_line_1,
                        "billing_add2": usr_addr.address_line_2,
                        "billing_pin": usr_addr.postal_code,
                        "billing_city": usr_addr.city,
                        "billing_state": usr_addr.state,
                        "billing_country": usr_addr.country,
                        "billing_phone": usr_addr.phone_no_1,
                        "billing_alt_phone": usr_addr.phone_no_2,
                        "billing_email": usr_addr.email,
                        "products": order_items,
                        "shipment_length": settings.PACKAGE_LENGTH,  # in cm
                        "shipment_width": settings.PACKAGE_BREADTH,  # in cm
                        "shipment_height": settings.PACKAGE_HEIGHT,  # in cm
                        "weight": settings.PACKAGE_WEIGHT,  # in Kg
                        "payment_mode": "Prepaid" if paymenttype == "ONLINE" else "COD",
                        "return_address_id": settings.SHIPMENT_RETURN_ADDR_ID_ITHINGS_LOGISTICS,
                        "store_id": settings.STORE_ID_ITHINGS_LOGISTICS
                    }
                ],
                "pickup_address_id": settings.PICKUP_ADDR_ID_ITHINGS_LOGISTICS,
                "access_token": settings.ACCESS_TOKEN_ITHINGS_LOGISTICS,
                "secret_key": settings.SECRET_KEY_ITHINGS_LOGISTICS,
                "logistics": logistic,
                "order_type":"forward"
            }
        }

        if paymenttype != "ONLINE":
            payload.update(
                {
                    "cod_amount": "300",
                }
                )
        
        if logistic == "fedex":
            payload.update(
                {
                    "s_type": "standard",
                }
            )

        payload_json = json.dumps(payload)
        response = requests.request("POST", url, headers=self.headers, data=payload_json)

        return response.json()

    # def GetOrder(self,oid,awb):
    #     url = self.base_url + f'/order/get_details.json'