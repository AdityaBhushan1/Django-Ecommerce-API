from django.utils import timezone

def get_current_date():
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime('%d-%m-%Y')
    return formatted_datetime


get_current_date()