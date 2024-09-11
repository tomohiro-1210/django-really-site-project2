from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

# Create your views here.
def article(request, pk):
    article = Article.objects.get(pk=pk)
    template = 'blog/article.html'
    context = {'article':article}
    return render(request, template, context)