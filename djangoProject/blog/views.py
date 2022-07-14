# importing post
from blog.models import *

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# a menu of viable actions
menu = ['about', 'add blog', 'feedback', 'log in']


# Created views


# categories
def show_category(request):
    return HttpResponse(f"showing category with id = ")


# created index
def index(request):     # HttpRequest
    posts = Post.objects.all()
    cats = Category.objects.all()

    # raising a 404 error
    if len(posts) == 0:
        raise Http404

    # creating a context
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        # 'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', {'posts': posts, 'menu': menu, 'title': 'Main Page'})


# created view which is for an 'about' page
def about(request):     # HttpRequest
    return render(request, 'blog/about.html', {'title': 'About'})


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