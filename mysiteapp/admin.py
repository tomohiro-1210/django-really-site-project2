from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Profile
from blog.models import Article

from mysite.forms import UserCreationForm

# Register your models here.
# プロフィールとユーザーの紐づけ
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# 管理画面のクラス、UserAdminをカスタマイズしたやつ
class CustonUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
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
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
    )
    
    add_form = UserCreationForm
    
# 管理画面の表示
admin.site.register(User, CustonUserAdmin)
admin.site.register(Profile)

# 管理画面の非表示
admin.site.unregister(Group)
