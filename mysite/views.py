from django.urls import include
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    template = 'mysite\index.html'
    context = {'articles':articles}
    return render(request, template, context)