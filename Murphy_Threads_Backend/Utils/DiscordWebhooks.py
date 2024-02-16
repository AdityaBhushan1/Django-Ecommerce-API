import requests
from datetime import datetime

def send_discord_message(webhook_url,tile,desciption,fields):

    current_time_utc = datetime.utcnow()
    timestamp_str = current_time_utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    payload = {
        "embed": {
            "title": tile,
            "description": desciption,
            # "color": 14560253,
            "timestamp": timestamp_str,
            "fields": fields
        }
    }

    requests.post(webhook_url, json=payload)