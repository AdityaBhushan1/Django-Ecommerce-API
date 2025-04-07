from django.utils import timezone


def get_current_datetime():
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
    return formatted_datetime


def get_current_date():
    current_date = timezone.localtime(timezone.now())
    formatted_date = current_date.strftime("%d-%m-%Y")
    return formatted_date
