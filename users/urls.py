"""Defines URL patterns for users"""
from django.urls import path, include
# from django.contrib.auth import views as auth_views  # - for default django log in and log out

from . import views
app_name = 'users'
urlpatterns = [
#  Include default auth urls.
path('', include('django.contrib.auth.urls')),

# log out view
# path('logout/', auth_views.LogoutView.as_view(), name='logout'), -# for default django log in and log out trigger
   
path('logged_out/', views.logged_out, name='logged_out'),   # Render the custom logged_out template view

# Registration page.
path('register/', views.register, name='register'),


]
















# ..........................NB...........................
# my own log in and log out
# path('logout/', views.custom_logout, name='logout'),  # Custom logout view
# path('logged_out/', views.logged_out, name='logged_out'),  # Custom logged out page



