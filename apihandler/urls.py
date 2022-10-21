from django.urls import path
from apihandler.views import index, websites, detail, users


urlpatterns = [
    path('', index),
    path('users/websites', websites),
    path('users/detail', detail),
    path('users', users),
]
