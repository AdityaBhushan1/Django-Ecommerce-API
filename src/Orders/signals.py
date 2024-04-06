from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from Payments.models import Payments
from Payments.Stripe.StripeHandler import createRefund as StripeRefund

@receiver(post_save, sender=Order)
def handel_order_status_update(sender, instance, **kwargs):
    if kwargs.get('update_fields') and 'status' in kwargs['update_fields']:
        if instance.status == 'RETURN_APPROVED':
            # Todo inform user with email that return request has been approved and guide them with further instrunctions
            returns = Return.objects.get(order=instance.id)  
            returns.update(status = "RETURN_APPROVED")
            
        elif instance.status == 'RETURN_REJECTED':
            # Todo inform user with email that return request has been rejected and provide them the reason
            returns = Return.objects.get(order=instance.id)  
            returns.update(status = "RETURN_REJECTED")

        elif instance.status == 'RETURNED':
            # Todo inform user with email that product has been returned and and they will recive refund in 5 to 10 bussiness days
            returns = Return.objects.get(order=instance.id)  
            pay = Payments.objects.get(order = instance.id)
            user = Users.objects.get(id = instance.user)

            returns.update(status = "RETURNED")
            ammount = ... #Todo calculate refund amount

            returns.udpate(return_recived_date = ...) #Todo date of returned date

            if instance.payment_mode == "ONLINE":
                if pay.payment_menthod == "STRIPE":
                    StripeRefund(
                        payid = pay.payment_id,
                        ammount = ammount,
                        oid = instance.id,
                        uid = user.id,
                    )
                elif pay.payment_menthod == "PAYPAL":
                    ...#Todo create paypal refund
                
                elif pay.payment_menthod == "INSTAMOJO":
                    ...#Todo create instamojo refund

            elif instance.payment_mode == "COD":
                ... #Todo email user to provide a refund method where we can refund the ammount
