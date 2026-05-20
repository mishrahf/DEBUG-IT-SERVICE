from django import template

register = template.Library()


@register.filter
def split(value, delimiter=','):
    """Split a string by a delimiter."""
    if not value:
        return []
    return value.split(delimiter)


@register.filter
def strip(value):
    """Remove leading and trailing whitespace."""
    if not value:
        return value
    return value.strip()
