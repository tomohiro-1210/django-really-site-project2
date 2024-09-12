from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# マイページ
def mypage(request):
    template = "mysite/mypage.html"
    context = {}
    return render(request, template, context)