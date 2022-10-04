import random
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="range")
def iterate(x):
    return range(x)

@register.filter(name="dice")
def dice(x):
    return random.randint(1, x)

