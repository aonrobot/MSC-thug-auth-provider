
from django.conf import settings
import requests

def create_client_application(consumer_id, app_name, redirect_uri):
    data = {
        "name": app_name,
        "redirect_uris": redirect_uri
    }

    url = "{}/consumers/{}/oauth2" . format(settings.KONG_ADMIN_URL, consumer_id)

    return requests.post(url, data)

def get_oauth_code(client_id, client_secret, user_id):

    provision_key = settings.OAUTH_SERVICE['provision_key']

    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "provision_key": provision_key,
        "authenticated_userid": user_id,
        "response_type": "code"
    }

    url = "{}/api/oauth2/authorize" . format(settings.KONG_URL)

    try:
        response = requests.post(url, data, headers={"x-forwarded-proto" : "https"})
        return response.json()
    except requests.exceptions.RequestException as e:
        print('request code to kong error')
        print(e)
        return 'kong error'

def get_oauth_token(client_id, client_secret, code):

    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code
    }

    url = "{}/api/oauth2/token" . format(settings.KONG_URL)

    try:
        response = requests.post(url, data, headers={"x-forwarded-proto" : "https"})
    except requests.exceptions.RequestException as e:
        print('request token to kong error')
        print(e)

    return response.json()

def get_oauth_refresh(client_id, client_secret, refresh_token):

    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token
    }

    url = "{}/api/oauth2/token" . format(settings.KONG_URL)

    try:
        response = requests.post(url, data, headers={"x-forwarded-proto" : "https"})
    except requests.exceptions.RequestException as e:
        print('request token to kong error')
        print(e)

    return response.json()