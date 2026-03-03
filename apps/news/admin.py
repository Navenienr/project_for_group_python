from django.contrib import admin
from .models import News
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at']