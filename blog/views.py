from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, Comment
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.
# 記事詳細
def article(request, pk):
    # 記事の個別データ引っ張り出し
    article = Article.objects.get(pk=pk)
    
    # コメントの引っ張り出し
    comments = Comment.objects.filter(article=article)
    
    # コメントの投稿
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            keep_comment = form.save(commit=False)
            keep_comment.user = request.user # ログインしているユーザーの情報を引き渡し
            keep_comment.article = article # 記事のデータを引き渡し
            keep_comment.save()
    
    # テンプレートページなどの読み込み
    template = 'blog/article.html'
    context = {
        'article':article,
        'comments':comments,
        }
    return render(request, template, context)

# 記事一覧
def blog_list(request):
    # 記事データの読み込み
    articles = Article.objects.all()
    # ページャー
    paginator = Paginator(articles, 5)
    page_num = request.GET.get('page')
    # テンプレートなどの設定
    template = 'blog/blog_list.html'
    context = {
        'articles':articles,
        'page_obj':paginator.get_page(page_num),
        'page_num':page_num
        }
    return render(request, template, context)