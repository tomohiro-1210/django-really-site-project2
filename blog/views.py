from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator

# Create your views here.
# 記事詳細
def article(request, pk):
    # 記事の個別データ引っ張り出し
    article = Article.objects.get(pk=pk)
    # テンプレートページなどの読み込み
    template = 'blog/article.html'
    context = {'article':article}
    return render(request, template, context)

# 記事一覧
def blog_list(request):
    # 記事データの読み込み
    articles = Article.objects.all()
    # ページャー
    paginator = Paginator(articles, 2)
    page_num = request.GET.get('page')
    # テンプレートなどの設定
    template = 'blog/blog_list.html'
    context = {
        'articles':articles,
        'page_obj':paginator.get_page(page_num),
        'page_num':page_num
        }
    return render(request, template, context)