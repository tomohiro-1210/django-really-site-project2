from django.shortcuts import render, redirect
from django.urls import path, include
from .views import article, blog_list

urlpatterns = [
    path('article/<int:pk>', article, name="article"),
    path('list', blog_list, name="blog_list"),
]
