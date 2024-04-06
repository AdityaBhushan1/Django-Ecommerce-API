from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.customer_details import CustomerDetails
from cashfree_pg.models.order_meta import OrderMeta
from django.conf import settings
from ..models import *

def CreateOrder(customer,oid,ammount):
    customerDetails = CustomerDetails(customer_id=customer.id, customer_phone=customer.phone_no)
    customerDetails.customer_name = customer.name
    customerDetails.customer_email = customer.email

    createOrderRequest = CreateOrderRequest(order_id=oid, order_amount=ammount, order_currency="INR", customer_details=customerDetails)

    orderMeta = OrderMeta()
    orderMeta.return_url = settings.SITE_DOMAIN + '/payment_success' #Todo change this url to actual url
    # orderMeta.notify_url = "https://www.cashfree.com/devstudio/preview/pg/webhooks/24076493"
    createOrderRequest.order_meta = orderMeta

    try:
        api_response = Cashfree().PGCreateOrder(settings.CASHFREE_API_VERSION, createOrderRequest, None, None)
        Payments.objects.create(
                    payment_method="CASHFREE",
                    order=oid,
                    user=customer.id,
                    ammount = ammount,
                    status = "PENDING"
                )
        return api_response.data.payment_session_id
    except Exception as e:
        print(e)