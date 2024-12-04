from django.contrib import admin
from .models import Article, Comment, Tag

class TagInline(admin.TabularInline):
    model = Article.tags.through
    
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline,]
    exclude = ['tags']

# Register your models here.
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)