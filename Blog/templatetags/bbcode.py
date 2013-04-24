from django import template
from postmarkup import render_bbcode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def     bbcode(value):
    return mark_safe(render_bbcode(value))


# @register.filter
# def     trunc_menu(value):
#     if len(value) > 15:
#         value = value[:12] + "..."
#     return (value)


# @register.filter
# def     trunc_index(value):
#     if len(value) > 1500:
#         value = value[:1500] + "..."
#     return (value)
