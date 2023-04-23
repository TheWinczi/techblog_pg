import pytz

from django import template


register = template.Library()


@register.filter
def datetime_term(comment):
    created_at = comment.created_at
    timezone = pytz.timezone('Europe/Warsaw')
    return created_at.astimezone(timezone).strftime("%Y-%m-%d %H:%M")
