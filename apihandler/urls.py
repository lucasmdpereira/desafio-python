from django.urls import path
from apihandler.views import index

urlpatterns = [
    path('', index)
]
