# import uuid
# from account.models import *
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from email import send_account_activation_email
# from account.models import *

# @receiver(post_save,sender = Users)
# def send_email_token(sender,instance,created,**kwargs):
#     try:
#         if created:
#             email_token = str(uuid.uuid4())
#             email = instance.token
#             send_account_activation_email(email,email_token)
#     except Exception as e:
#         print(e)

# from django.core.mail import EmailMessage
# import os

# class Util:
#   @staticmethod
#   def send_email(data):
#     email = EmailMessage(
#       subject=data['subject'],
#       body=data['body'],
#       from_email=os.environ.get('EMAIL_FROM'),
#       to=[data['to_email']]
#     )
#     email.send()
