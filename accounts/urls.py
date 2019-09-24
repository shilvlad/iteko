from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('chpwd/', views.user_chpwd, name='user_chpwd'),
    path('signup/', views.user_signup, name='user_signup'),
]