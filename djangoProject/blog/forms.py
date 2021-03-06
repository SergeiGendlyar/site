from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

# old AddPostForm class
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Title', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255)
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     is_published = forms.BooleanField(label='Publish?', required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='category', empty_label='category not chosen')


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'choose category'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 250:
            raise ValidationError('length exceeds 250 symbols')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email,', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))