from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from blog.models import Article

# Register your models here.
# 管理画面のクラス、UserAdminをカスタマイズしたやつ
class CustonUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
                )
            }),
        (None, {
            'fields': (
                'is_active',
                'is_admin'
                )
            }),
    )
    
    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    
# 管理画面の表示
admin.site.register(User)
admin.site.register(Article)

# 管理画面の非表示
admin.site.unregister(Group)
