from django.urls import include, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from blog.models import Article
from .forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    ranks = Article.objects.order_by('-count')[:2]
    articles = Article.objects.all()[:3]
    template = 'mysite\index.html'
    context = {
        'articles':articles,
        'ranks':ranks,
        }
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
        # ログイン処理が成功したとき
        if form.is_valid():
            #　ログイン処理
            user = form.save(commit=False)
            user.save()
            # メッセージ
            messages.success(request, '登録が完了しました！ログインしてください。')
            return redirect('/')
    return render(request, template, context)

# ログインビュー
class Login(LoginView):
    template_name = 'mysite/login.html'
    
    # ログインが成功した時の処理
    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了！')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'ログインができませんでした。メールアドレスまたはパスワードが間違っています。')
        return super().form_invalid(form)    
    
    