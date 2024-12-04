from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# マイページ
@login_required
def mypage(request):
    # テンプレートの読み込み
    template = "mysite/mypage.html"
    context = {}
    # フォームからのデータ受け取り
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        # フォームの送信が成功したときの処理
        if form.is_valid():
           keep_profile = form.save(commit=False)
           keep_profile.user = request.user
           keep_profile.save()
           messages.success(request, "プロフィールの更新完了！")
    
    return render(request, template, context)