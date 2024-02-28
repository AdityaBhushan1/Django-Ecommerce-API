from django.utils import timezone

def get_current_datetime():
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')
    return formatted_datetime