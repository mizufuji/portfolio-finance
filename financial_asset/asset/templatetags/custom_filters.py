from django import template
import locale

register = template.Library()


@register.filter
def zip_lists(list1, list2):
    return zip(list1, list2)


@register.filter
def format_number(value):
    try:
        return "{:,.0f}".format(value)
    except (ValueError, TypeError):
        return value
