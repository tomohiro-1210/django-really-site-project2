from django.db import models
from django.contrib.auth import get_user_model

# ユーザーのプロフィール
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(default="匿名ユーザー", max_length=30)
    zipcode = models.CharField(default="",max_length=10)
    prefecture = models.CharField(default="", max_length=6)
    city = models.CharField(default="", max_length=10)
    address = models.CharField(default="", max_length=150)