from django import template

register = template.Library()

@register.filter(name='status')
def status(valor):
    match valor:
        case "ok":
            return "Alineable"
        case "injured":
            return "Lesionado"
        case "suspended":
            return "Suspendido"
        case "doubtful": 
            return "Dudoso"
        
