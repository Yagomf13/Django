from django import template
from pages.models import Page

#! Definimos nuestra template tag personaliza
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages