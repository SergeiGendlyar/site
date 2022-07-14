from django.contrib import admin

# Register your models here.
from .models import Post


# creating an PostAdmin Class
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)