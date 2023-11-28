# custom_filters.py
from django import template
import re

register = template.Library()

@register.filter(name='filter_description')
def filter_description(value):
    cleaned_description = re.sub(r'[^a-zA-Z ]', '', value)
    return cleaned_description
