"""
Сериализаторы модуля новостей.
"""
from rest_framework import serializers
from .models import News, Comment
from apps.core.serializers import UserProfileSerializer


class NewsSerializer(serializers.ModelSerializer):
    # Сериализатор для новостей
    class Meta:
        model = News
        fields = '__all__'

        # Только для чтения
        read_only_fields = ['author', 'views_count',
                            'created_at', 'updated_at', 'published_at']


class CommentSerializer(serializers.ModelSerializer):
    # Сериализатор для комментариев
    author = UserProfileSerializer(read_only=True)

    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'news',
            'author',
            'content',
            'created_at',
            'updated_at',
            'is_edited',
            'is_deleted',
            'can_edit',
            'can_delete'
        ]
        extra_kwargs = {
            'content': {'max_length': 1000}
        }

        read_only_fields = ['author', 'created_at', 'updated_at', 'is_edited', 'is_deleted']

    def get_can_edit(self, obj):
        # Проверка, может ли пользователь редактировать комментарий
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user.id == obj.author.id
        return False
    
    def get_can_delete(self, obj):
        # Проверка, может ли пользователь удалить комментарий
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # Пользователь может удалять свои комментарии
            if obj.author.id == request.user.id:
                return True
            # Модераторы и администраторы могут удалять любые комментарии
            if request.user.is_moderator:
                return True
            if request.user.is_superuser:
                return True
        return False