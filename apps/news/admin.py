from django.contrib import admin
from .models import News, Comment
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'author', 'created_at', 'is_deleted','short_content']

    list_filter = ['is_deleted', 'created_at']

    def short_content(self, obj):
        return obj.content[:100]

    short_content.short_description = 'Комментарий'