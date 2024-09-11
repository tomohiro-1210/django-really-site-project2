from django.urls import include
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'mysite\index.html'
    context = {}
    return render(request, template, context)