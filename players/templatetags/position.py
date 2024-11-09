from django import template

register = template.Library()

@register.filter(name='position')
def position(valor):
    val = int(valor)
    match val:
        case 1:
            return "por"
        case 2: 
            return "def"
        case 3: 
            return "cen"
        case 4:
            return "del"

