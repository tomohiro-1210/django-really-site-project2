from django.shortcuts import render, redirect
from django.urls import path, include
from .views import article

urlpatterns = [
    path('article/<int:pk>', article, name="article"),
]
