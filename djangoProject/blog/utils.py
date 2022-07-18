from blog.models import Category

menu =[{'title': 'about', 'url_name': 'about'},
       {'title': 'add page', 'url_name': 'add_page'},
       {'title': 'feedback', 'url_name': 'feedback'}]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cats_selected' not in context:
            context['cat_selected'] = 0
        return context