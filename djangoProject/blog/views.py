# importing post
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from blog.forms import AddPostForm, RegisterUserForm
from blog.models import *
from blog.utils import DataMixin




# legacy code at this point
#
# # a menu of viable actions
menu = [{'title': 'about', 'url_name': 'about'},
        {'title': 'add post', 'url_name': 'add_page'},
        {'title': 'feedback', 'url_name': 'feedback'},
        {'title': 'log in', 'url_name': 'login'}]


# Created views
# for contact
def feedback(request):
    return HttpResponse('Feedback')


# adding a page
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'title': 'add page'})


# for showing the login
def login(request):
    return HttpResponse('Log In')


# for showing the id of some post
def show_post(request, post_slug):
    post = get_object_or_404(Post, pk=post_slug)

    context = {
        'posts': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'blog/post.html', context=context)

# categories
def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

# context
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'themed view',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)


# created index
def index(request):     # HttpRequest
    posts = Post.objects.all()

    # raising a 404 error
    if len(posts) == 0:
        raise Http404

    # creating a context
    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        # 'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)


# created view which is for an 'about' page
def about(request):     # HttpRequest
    return render(request, 'blog/about.html', {'menu': menu,'title': 'About'})


# created categories
def categories(request, theme):
    print(request.GET)
    return HttpResponse(f'<h1>Blog themes<h1><p>{theme}</p>')
# http://127.0.0.1:8000/blog/themes/2021/?name=Gagarin&theme=rocket


# created archive of previous blogs
def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive of blogs for this year</h1><p>{year}</p>')


# created a 404 error handler
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Sorry, but the page appears to be not found</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')


# class LoginUser(DataMixin, LoginView):
#     from_class=AuthenicationForm
#     template_name = 'blog/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Log in")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('home')