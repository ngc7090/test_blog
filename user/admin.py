from django.contrib import admin
from .models import Article, Tag, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


admin.site.register(Article, ArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Tag, TagAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user')


admin.site.register(Comment, CommentAdmin)
