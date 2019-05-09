from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template.loader import get_template

#import ldap
from ldap3 import Server, Connection, ALL

import json

from app import forms
from app import kong

def index(request):
    # t = get_template('home.html')
    # html = t.render()
    return render(request, 'home.html')

@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    ldap_server = "ldap://metrosystems.co.th"

    data = json.loads(request.body.decode("utf-8").replace("\'", "\""))

    username = data["username"] + "@metrosystems.co.th"
    password = data["password"]
    client_id = data["client_id"]
    client_secret = data["client_secret"]

    try:
        server = Server("metrosystems.co.th", get_info=ALL)
        print(username, password)
        c = Connection(server, user=username, password=password)
        if not c.bind():
            print('error in bind', c.result)
            return JsonResponse({'login': False, 'data': '', 'error': ''})
        else:
            try:
                redirect_uri = kong.get_oauth_code(client_id, client_secret, username)
                print('login success')
                return JsonResponse({'login': True, 'data': redirect_uri["redirect_uri"], 'error': ''})
            except:
                return HttpResponse("get_oauth_code error")
            return HttpResponse("Password success " + username + " : " + password)
    except:
        return HttpResponse("Ldap connect error")

@csrf_exempt
@require_http_methods(['POST'])
def token(request):
    data = json.loads(request.body.decode("utf-8").replace("\'", "\""))
    
    try:
        client_id = data["client_id"]
        client_secret = data["client_secret"]
        code = data["code"]
    except:
        return JsonResponse({'error': 'Parameter Mei Mee'})

    token = kong.get_oauth_token(client_id, client_secret, code)

    return JsonResponse({'data': token, 'error': ''})

@csrf_exempt
@require_http_methods(['POST'])
def refresh(request):
    data = json.loads(request.body.decode("utf-8").replace("\'", "\""))

    try:
        client_id = data["client_id"]
        client_secret = data["client_secret"]
        refresh_token = data["refresh_token"]
    except:
        return JsonResponse({'error': 'Parameter Mei Mee'})

    token = kong.get_oauth_refresh(client_id, client_secret, refresh_token)

    return JsonResponse({'data': token, 'error': ''})

@login_required
@require_http_methods(['GET', 'POST'])
def create_application(request):

    user_id = User.objects.get(username=request.user).pk

    if request.method == 'POST':
        application_form = forms.ClientApplicationForm(request.POST)
        if application_form.is_valid():
            result = application_form.save('newerp_consumer')
            return HttpResponse(result)

    else:
        data = {
            "username": request.user.username,
            "custom_id": user_id,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
            "consumer": "newerp_consumer" 
        }

        application_form = forms.ClientApplicationForm(initial=data)

    context = {
        "application_form": application_form,
        "username" : user_id
    }

    return render(request, 'application.html', context)