import requests
import json
from Utils.GetCurrentDateTime import get_current_datetime
from django.conf import settings
from Users.models import *
from Orders.models import *
from django.utils import formats


class ShiprocketWrapper:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://apiv2.shiprocket.in/v1/external"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

    def CreateOrder(self, oid, user, baddrid, saddrid, paymenttype, price):
        url = self.base_url + "/orders/create"

        b_usr_addr = UserAddresses.objects.get(id=baddrid)
        order_item = OrderItem.objects.filter(order=oid)

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
            "weight": settings.PACKAGE_WEIGHT,
        }

        if baddrid != saddrid:
            s_usr_addr = UserAddresses.objects.get(id=saddrid)

            payload.update(
                {
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
                }
            )
        else:
            payload.update(
                {
                    "shipping_is_billing": True,
                }
            )

        payload_json = json.dumps(payload)
        response = requests.request(
            "POST", url, headers=self.headers, data=payload_json
        )

        return response.json()

    def CancelOrder(self, oid):
        url = self.base_url + "/orders/cancel"

        payload = {"ids": [oid]}

        payload_json = json.dumps(payload)
        response = requests.request(
            "POST", url, headers=self.headers, data=payload_json
        )

        return response.json()

    def GenrateAWB(self, shipmentid):
        url = self.base_url + "/courier/assign/awb"

        payload = {
            "shipment_id": shipmentid,
        }

        payload_json = json.dumps(payload)
        response = requests.request(
            "POST", url, headers=self.headers, data=payload_json
        )

        return response.json()

    def GetOrderDetails(self, oid):
        url = self.base_url + f"/orders/show/{oid}"

        payload = {}

        payload_json = json.dumps(payload)
        response = requests.request("GET", url, headers=self.headers, data=payload_json)

        return response.json()

    def CreateReturn(self, oid, odate, sid, paymentmode, price):
        url = self.base_url + "/orders/create/return"

        s_addr = UserAddresses.objects.get(id=sid)
        order_item = OrderItem.objects.filter(order=oid)

        order_items = []

        for item in order_item:
            item_data = {
                "name": item.product.name,
                "qc_enable": True,
                "qc_product_name": item.product.name,
                "sku": item.product.sku,
                "units": item.quantity,
                "selling_price": item.product.sale_price,
                "qc_brand": settings.SITE_NAME,
                "qc_product_image": item.product.main_image,
                "qc_color": item.color.color_nickname,
                "qc_size": item.size.size,
            }
            order_items.append(item_data)

        payload = {
            "order_id": oid,
            "order_date": formats.date_format(odate, "Y-m-d"),
            "channel_id": settings.SHIPROCKET_CHANNEL_ID,
            "pickup_customer_name": s_addr.first_name,
            "pickup_last_name": s_addr.last_name,
            "pickup_address": s_addr.address_line_1,
            "pickup_address_2": s_addr.address_line_2,
            "pickup_city": s_addr.city,
            "pickup_state": s_addr.state,
            "pickup_country": s_addr.country,
            "pickup_pincode": s_addr.postal_code,
            "pickup_email": s_addr.email,
            "pickup_phone": s_addr.phone_no_1,
            "shipping_customer_name": settings.RETURN_SELLER_NAME,
            "shipping_address": settings.RETURN_SELLER_ADDR,
            "shipping_city": settings.RETURN_SELLER_CITY,
            "shipping_country": settings.RETURN_SELLER_COUNTRY,
            "shipping_pincode": settings.RETURN_SELLER_POSTCODE,
            "shipping_state": settings.RETURN_SELLER_STATE,
            "shipping_email": settings.RETURN_SELLER_EMAIL,
            "shipping_phone": settings.RETURN_SELLER_PHNO,
            "order_items": order_items,
            "payment_method": "PREPAID" if paymentmode == "ONLINE" else "COD",
            "sub_total": price,
            "length": settings.PACKAGE_LENGTH,
            "breadth": settings.PACKAGE_BREADTH,
            "height": settings.PACKAGE_HEIGHT,
            "weight": settings.PACKAGE_WEIGHT,
        }

        payload_json = json.dumps(payload)
        response = requests.request(
            "POST", url, headers=self.headers, data=payload_json
        )

        return response.json()

    def GetShipmentDetails(self, sid):
        url = self.base_url + f"/shipments/{sid}"

        payload = {}

        payload_json = json.dumps(payload)
        response = requests.request("GET", url, headers=self.headers, data=payload_json)

        return response.json()

    def CancelShipment(self, awb):
        url = self.base_url + f"/orders/cancel/shipment/awbs"

        payload = {
            "awbs": [
                awb,
            ]
        }

        payload_json = json.dumps(payload)
        response = requests.request(
            "POST", url, headers=self.headers, data=payload_json
        )

        return response.json()

    def GetTrackingDetails(self, awb_code):
        url = self.base_url + f"/courier/track/awb/{awb_code}"

        payload = {}

        payload_json = json.dumps(payload)
        response = requests.request("GET", url, headers=self.headers, data=payload_json)

        return response.json()

    def GetTrackingDetailsViaSID(self, sid):
        url = self.base_url + f"/courier/track/shipment/{sid}"

        payload = {}

        payload_json = json.dumps(payload)
        response = requests.request("GET", url, headers=self.headers, data=payload_json)

        return response.json()
