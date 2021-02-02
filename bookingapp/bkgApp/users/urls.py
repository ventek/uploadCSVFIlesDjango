from django.urls import path

from .views import profile, about

app_name = 'users'

urlpatterns = [
    path('profile', profile, name='profile'),
    path('about', about, name='about'),
]
