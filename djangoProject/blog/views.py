# importing post
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from blog.forms import AddPostForm, RegisterUserForm, LoginUserForm
from blog.models import *
from blog.utils import DataMixin




# legacy code at this point
#
# # a menu of viable actions
menu = [{'title': 'about', 'url_name': 'about'},
        {'title': 'add post', 'url_name': 'add_page'},
      ]


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign Up')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign In')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


def logout_user(request):
    logout(request)
    return redirect('login')


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add page'
        context['menu'] = menu
        return context


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

# Created views


# for feedback page
def feedback(request):
    return HttpResponse('Feedback')




# created view which is for an 'about' page

def about(request):     # HttpRequest
    return render(request, 'blog/about.html', {'menu': menu,'title': 'About'})


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
        'title': 'view by category',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)


# created categories
def categories(request, theme):
    print(request.GET)
    return HttpResponse(f'<h1>Blog themes<h1><p>{theme}</p>')
# http://127.0.0.1:8000/blog/themes/2021/?name=Gagarin&theme=rocket <-- example


# created archive of previous blogs
def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive of blogs for this year</h1><p>{year}</p>')


# created a 404 error handler
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Sorry, but the page appears to be not found</h1>')


# class PostCategory(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Post.objects.filter(cat_id=self.kwargs['cat_id'], is_published=True)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Category - ' + str(context['posts'][0].cat)
#         context['menu'] = menu
#         context['cat_selected'] = context['posts'][0].cat_id
#         return context



# legacy stuff
# # adding a page
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'blog/addpage.html', {'form': form, 'title': 'add page'})
# another part of legacy code
# # for showing the id of some post
# def show_post(request, post_slug):
#     post = get_object_or_404(Post, pk=post_slug)
#
#     context = {
#         'posts': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'blog/post.html', context=context)

# also legacy stuff
# # created index
# def index(request):     # HttpRequest
#     posts = Post.objects.all()
#
#     # raising a 404 error
#     if len(posts) == 0:
#         raise Http404
#
#     # creating a context
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Main Page',
#         # 'cat_selected': cat_id,
#     }
#
#     return render(request, 'blog/index.html', context=context)
#
# for showing the login
# def login(request):
#     return HttpResponse('Log In')



