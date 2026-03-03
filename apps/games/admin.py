from django.contrib import admin
from .models import Game, Genre, Language

admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres', 'interface_language', 'voice_language')
    list_display = ('name', 'developer', 'created_at')
    search_fields = ('name', 'developer')
