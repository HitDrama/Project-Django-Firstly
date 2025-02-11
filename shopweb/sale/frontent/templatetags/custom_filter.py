from django import template
from html import unescape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='html_decape')
def html_decape(value):
    return mark_safe(unescape(value))
