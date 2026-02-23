"""
Сериализаторы модуля новостей.
"""
from rest_framework import serializers
from apps.news.models import News, Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории новостей"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class NewsListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка новостей (краткая информация)"""
    category = CategorySerializer(read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = [
            'id', 'title', 'slug', 'short_description', 
            'image', 'category', 'author_username',
            'views_count', 'likes_count', 'is_liked',
            'created_at', 'published_at'
        ]
    
    def get_likes_count(self, obj):
        """Количество лайков"""
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        """Проверка, лайкнул ли текущий пользователь"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False


class NewsDetailSerializer(NewsListSerializer):
    """Сериализатор для детальной информации о новости"""
    class Meta(NewsListSerializer.Meta):
        fields = NewsListSerializer.Meta.fields + ['content', 'updated_at', 'is_published']


class NewsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новости"""
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'short_description', 'category', 'image', 'is_published']
    
    def validate_title(self, value):
        """Валидация заголовка"""
        if len(value) < 5:
            raise serializers.ValidationError("Заголовок должен содержать минимум 5 символов")
        return value
    
    def validate_content(self, value):
        """Валидация содержания"""
        if len(value) < 50:
            raise serializers.ValidationError("Содержание должно содержать минимум 50 символов")
        return value




