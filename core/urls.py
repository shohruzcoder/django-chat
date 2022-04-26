from os import urandom
from re import template
from django.urls import path
from .views import frontpage, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontpage, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]
