from django import template
from django.utils.safestring import mark_safe

from ningen.interview.utils import ningen_markdown as md

register = template.Library()


@register.filter
def markdown(value):
    return mark_safe(md.convert(value))
