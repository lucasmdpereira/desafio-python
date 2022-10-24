from django.http.response import HttpResponse
from django.template import loader
from src.handlers.dataHandler import DataAPI 
#import json

def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    template = loader.get_template('apihandler/index.html')
    context = {
        'num_visits': num_visits,
    }
    return HttpResponse(template.render(context, request))

def websites(request):
    # template = loader.get_template('apihandler/websites.html')
    context = {
        'websites': DataAPI().list_users_websites,
    }
    return HttpResponse(context['websites'])


def detail(request):
    # template = loader.get_template('apihandler/detail.html')
    context = {
        'users': DataAPI().list_users_name_email_company,
    }
    return HttpResponse(context['users'])

def users(request):
    # template = loader.get_template('apihandler/detail.html')
    context = {
        'users': DataAPI().list_users_by_query('cle'),
    }
    return HttpResponse(context['users'])