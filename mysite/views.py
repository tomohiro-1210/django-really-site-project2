from django.urls import include, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from blog.models import Article
from .forms import UserCreationForm

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

# ログアウト
def custom_logout(request):
    logout(request)
    return redirect('login')

# 新規登録
def signup(request):
    template = 'mysite/signup.html'
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    return render(request, template, context)

# ログインビュー
class Login(LoginView):
    template_name = 'mysite/login.html'
    