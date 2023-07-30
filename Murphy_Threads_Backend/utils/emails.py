from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_activation_email(recipient_email, activation_url):
    subject = 'Activate your account on '+settings.SITE_NAME
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]


    text_content = activation_url
    sent_mail = send_mail(
                subject,
                text_content,
                from_email,
                to,
                fail_silently=False,
            )

# def send_reset_password_email(recipient_email, reset_url):
#     subject = 'Reset Your Password on '+settings.SITE_NAME
#     from_email = settings.EMAIL_HOST_USER
#     to = [recipient_email]
    
#     text_content = reset_url
#     email = EmailMultiAlternatives(subject, text_content, from_email, to)
#     email.attach_alternative(html_content, "text/html")
#     email.send()