from http.client import HTTPResponse
from django.shortcuts import render

def index(request):
    return render(request, 'apihandler/index.html')

def websites(request):
    return render(request, 'apihandler/websites.html')

def detail(request):
    return render(request, 'apihandler/detail.html')

def users(request):
    return render(request, 'apihandler/users.html')