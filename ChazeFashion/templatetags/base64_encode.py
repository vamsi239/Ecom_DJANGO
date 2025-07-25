# catalog/templatetags/base64_encode.py
import base64
from django import template

register = template.Library()

@register.filter
def b64encode(value):
    if value:
        return base64.b64encode(value).decode()
    return ''
