from django.shortcuts import render, redirect
from django.urls import path, include
from .views import mypage

urlpatterns = [
    path('mypage/', mypage, name="mypage"),
]
