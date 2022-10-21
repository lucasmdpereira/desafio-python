from django.http.response import HttpResponse
from django.template import loader
from src.handlers.dataHandler import DataAPI 
import json

def index(request):
    template = loader.get_template('apihandler/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def websites(request):
    template = loader.get_template('apihandler/websites.html')
    context = {
        'websites': DataAPI().list_users_websites,
    }
    return HttpResponse(template.render(context, request))


def detail(request):
    template = loader.get_template('apihandler/detail.html')
    context = {
        'users': DataAPI().list_users_name_email_company,
    }
    return HttpResponse(template.render(context, request))

def users(request):
    template = loader.get_template('apihandler/detail.html')
    context = {
        'users': DataAPI().list_users_by_query('cle'),
    }
    return HttpResponse(template.render(context, request))