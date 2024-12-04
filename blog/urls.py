from django.shortcuts import render, redirect
from django.urls import path, include
from .views import article, blog_list, blog_tags

urlpatterns = [
    path('list', blog_list, name="blog_list"),
    path('article/<int:pk>', article, name="article"),
    path('tags/<slug:slug>', blog_tags, name="blog_tags"), 
]
