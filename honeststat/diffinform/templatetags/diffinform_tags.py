from django import template
from diffinform.models import *
from diffinform.views import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('diffinform/list_categories.html')
def show_categories(cat_selected):
    cats = Category.objects.all()
    return {"cats": cats, 'cat_selected': cat_selected}

@register.inclusion_tag('diffinform/list_menu.html')
def show_menu(menu=menu):
    return {"menu": menu}