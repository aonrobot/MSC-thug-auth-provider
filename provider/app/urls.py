from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r'login', views.login, name="login"),
    path(r'token', views.token, name="token"),
    path(r'refresh', views.refresh, name="refresh")
]
