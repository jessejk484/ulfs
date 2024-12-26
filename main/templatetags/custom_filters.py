from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def custom_timestamp_format(timestamp):
    now = timezone.now()
    if timestamp.date() == now.date():
        # Timestamp is from today
        formatted_time = timestamp.strftime("%I:%M %p")  # Format as "7:51 PM"
        return f"Today {formatted_time}"
    elif timestamp.date() == now.date() - timedelta(days=1):
        # Timestamp is from yesterday
        formatted_time = timestamp.strftime("%I:%M %p")  # Format as "7:51 PM"
        return f"Yesterday {formatted_time}"
    else:
        # Timestamp is older than yesterday, use the original timestamp format
        return timestamp.strftime("%Y-%m-%d %I:%M %p")  # Format as "2023-01-15 7:51 PM"
