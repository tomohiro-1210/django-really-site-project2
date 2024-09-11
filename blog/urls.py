from django.shortcuts import render, redirect
from django.urls import path, include
from .views import blog

urlpatterns = [
    path('', blog, name="blog"),
]
