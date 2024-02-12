from django.conf import settings
import stripe

stripe.api_key(settings.STRIPE_SECRET_KEY)

# def create_checkout_session(return_url,success_url,cart_id,user,email,expiry,price):
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items = [
#                 {
#                     'price_data':{
#                         'currency':'inr',
#                         'unit_ammount':price,
#                         'product_data':{
#                             'name':f'Cart ID: {cart_id}'
#                         },
#                         'quantity':1
#                     }
#                 }
#             ],
#             mode='payment',
#             return_url = return_url,
#             success_url = success_url,
#             client_reference_id = cart_id,
#             customer = user,
#             customer_email = email,
#             expires_at = expiry,
#         )
#     except Exception as e:
#         return str(e)

#     return(checkout_session.id)