from django.contrib import admin
from django.urls import path, include
from .views import posts_view, add_new_post_view


urlpatterns = [
    path('posts/', posts_view),
    path('posts/add/', add_new_post_view)
]
