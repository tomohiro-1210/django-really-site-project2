from django.urls import include
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[:3]
    template = 'mysite\index.html'
    context = {'articles':articles}
    return render(request, template, context)

# ログイン
def login(request):
    # テンプレートなど
    template = "mysite/login.html"
    context = {}
    # フォームからデータを受け取る
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    return render(request, template, context)