from email import message
import imp
from urllib import request
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect, render
from post.models import Blog
from .forms import createBlog
from .forms import RegistrationForm

# Create your views here.

def User_registration(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form}
    return render(request, 'post/login_register.html' , context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check User Exist
        # try:
        #     user  = User.objects.get(username = username)
        # except:
        #     messages.error(request, 'user does not Exist .')

        user  = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password invalid')
    context = {'page' : page}
    return render(request, 'post/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


















def home(request):
    blogs = Blog.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'post/home.html' , context) 

def blog(request):
    return render(request, 'post/blog.html') 

def profile(request, pk):
    blog_id = Blog.objects.get(id = pk)
    context = {'blog_id' : blog_id}
    return render(request, 'post/profile.html', context) 

def upload(request):
    upload = createBlog()
    if request.method == 'POST':
        upload = createBlog(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid data")
    else:
        return render(request, 'post/upload_form.html', {'upload_form': upload})
