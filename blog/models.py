from django.db import models

# Create your models here.
# 記事のDBモデル
class Article(models.Model):
    title = models.CharField(default="",blank=True, max_length=30)
    text = models.TextField(default="", )
    author = models.CharField(default="", max_length=30)
    create_at = models.DateTimeField(auto_now_add=True) # auto_now_addは一度データが追加されたときに登録される
    update_at = models.DateTimeField(auto_now=True) # auto_nowは更新された時に登録・更新される
    