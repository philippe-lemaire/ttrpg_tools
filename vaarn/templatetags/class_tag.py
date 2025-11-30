# Source - https://stackoverflow.com/a
# Posted by davidtingsu, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-30, License - CC BY-SA 4.0

from django import template

register = template.Library()


@register.filter(name="get_class")
def get_class(value):
    return value.__class__.__name__
