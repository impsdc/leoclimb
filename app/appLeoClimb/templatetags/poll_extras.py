from django import template
import re
from pprint import pprint
register = template.Library()

def regex(text):
    return re.findall(r'\d+', text)

@register.filter
def orderbyplace(self):
    helo = list(self)
    filtered = helo.sort(key=lambda x: regex(x.place))
    return helo

@register.filter()
def debug(self):
    pprint(vars(self))
    return self