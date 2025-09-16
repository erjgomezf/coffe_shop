from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    """
    Multiplica el valor por el argumento.
    Además, maneja errores si los valores no son numéricos.
    Uso en plantilla: {{ value|multiply:arg }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ""
