from django.contrib import admin
from django.urls import path
from .views import create_account_view, login_view, logout_handler

urlpatterns = [
    path('create/', create_account_view),
    path('login/', login_view),
    path('logout/', logout_handler)
]
