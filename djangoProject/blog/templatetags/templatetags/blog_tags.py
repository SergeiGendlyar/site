from django import template
from blog.models import *


register = template.Library()


# writing a getter for a category
@register.inclusion_tag('blog/list_categories.html')
def get_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}