from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# 記事のDBモデル
class Article(models.Model):
    title = models.CharField(default="",blank=True, max_length=30)
    text = models.TextField(default="", )
    author = models.CharField(default="", max_length=30)
    create_at = models.DateTimeField(auto_now_add=True) # auto_now_addは一度データが追加されたときに登録される
    update_at = models.DateTimeField(auto_now=True) # auto_nowは更新された時に登録・更新される
    
# コメントモデル
class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
# OnetoOne １対１
# ForeignKey 1対多
# ManytoMany 多対多
