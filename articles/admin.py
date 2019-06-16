from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('id', 'reference_id', 'author', 'heading', 'content', 'image', 'file', 'visits', 'tags')
    list_filter = ('author',)


admin.site.register(Article, ArticleAdmin)
