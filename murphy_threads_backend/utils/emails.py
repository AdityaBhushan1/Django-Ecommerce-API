from django.conf import settings
from django.core.mail import send_email


# Todo create a email template
def send_account_activation_email(email,email_token):
    subject = "Account Activation Required For Your Murphy Threads Account"
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi,Click On The Link To Activate Your Account:- \nhttps://murphythreads.store/account/activate/{email_token}'

    send_email(subject,message,email_from,[email])