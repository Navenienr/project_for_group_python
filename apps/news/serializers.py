"""
Сериализаторы модуля новостей.
"""
from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['author', 'views_count',
                            'created_at', 'updated_at', 'published_at']




