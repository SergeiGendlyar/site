from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # same as in META class, we change this thing, for the sake of uniformity, it is kept in English
    verbose_name = 'user posts'