from pyexpat import model
from statistics import mode
from attr import fields
from django import forms
from post.models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']