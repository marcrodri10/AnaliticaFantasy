from django import template

register = template.Library()

@register.filter(name='number')
def number(valor):
    val = int(valor)
    val_comma = "{:,}".format(val)
    val_point = val_comma.replace(",",".")
    return val_point
