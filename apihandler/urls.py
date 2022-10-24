
from django.urls import path, include
from apihandler.views import index, websites, detail, users

urlpatterns = [
    path('', index),
    path('users/websites', websites, name='websites'),
    path('users/detail', detail, name='detail'),
    path('users', users, name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
]
