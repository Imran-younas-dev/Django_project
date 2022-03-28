from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [ 
    path('home/',views.home, name = 'home'),
    path('blog/',views.blog, name = 'blog'),
    path('upload/' , views.upload, name= "upload"),
    path('profile/<str:pk>/' , views.profile, name= "profile"),
    path('', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.User_registration, name = 'register')

]