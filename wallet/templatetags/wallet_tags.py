from django import template

register = template.Library()

@register.filter
def timestamp_to_time(timestamp):
    """Converts a timestamp into datetime obj"""
    import datetime
    return datetime.datetime.fromtimestamp(timestamp)

