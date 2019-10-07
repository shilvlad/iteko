from django.contrib import admin
from django.contrib.auth import views as v
from django.urls import include, path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('chpwd/', views.user_chpwd, name='user_chpwd'),
    path('chpwd/', v.PasswordChangeView.as_view(), name='password_change'),
    path('chpwd/done/', v.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('signup/', views.user_signup, name='user_signup'),
    path('profile/', views.user_profile, name='user_profile'),
]