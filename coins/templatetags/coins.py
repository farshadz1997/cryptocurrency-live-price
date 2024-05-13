from django import template 
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def color_tag(value):
    final_value = round(value, 2)
    if final_value < 0:
        return "red"
    elif final_value == 0:
        return "black"
    else:
        return "green"
    