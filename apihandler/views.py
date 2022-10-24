from django.http.response import HttpResponse
from django.template import loader
from src.handlers.dataHandler import DataAPI
from django.contrib.auth.decorators import login_required 
#import json


@login_required
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    template = loader.get_template('apihandler/index.html')
    context = {
        'num_visits': num_visits,
    }
    return HttpResponse(template.render(context, request))

@login_required
def websites(request):
    # template = loader.get_template('apihandler/websites.html')
    context = {
        'websites': DataAPI().list_users_websites,
    }
    return HttpResponse(context['websites'])

@login_required
def detail(request):
    # template = loader.get_template('apihandler/detail.html')
    context = {
        'users': DataAPI().list_users_name_email_company,
    }
    return HttpResponse(context['users'])

@login_required
def users(request):
    # template = loader.get_template('apihandler/detail.html')
    query = ''
    if request.GET.getlist("name"):
        query = request.GET.getlist("name")[0]
    
    print(query)
    
    context = {
        'users': DataAPI().list_users_by_query(query),
    }
    return HttpResponse(context['users'])