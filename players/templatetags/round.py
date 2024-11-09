from django import template

register = template.Library()

@register.filter(name='round')
def number(valor):
    val = round(valor, 2)
    
    return val
