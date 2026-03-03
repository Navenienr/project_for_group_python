from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer
import telebot
from django.conf import settings
from django.utils import timezone


User = get_user_model()

TOKEN = '8733942341:AAGEpWvQnvvkMfaLLcO31TVRQ57RkpFj3cA'

bot = telebot.TeleBot(TOKEN)


class IsModeratorUser(permissions.BasePermission):
    # Разрешение для модераторов (нужно для создания постов)
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_moderator:
            return True
        return False



class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        # Проверка разрешений для публикации новости
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser | IsModeratorUser]
        else:
            self.permission_classes = [permissions.AllowAny]

        return super().get_permissions()
    



    def perform_create(self, serializer):
        # Публикация новости
        news = serializer.save(
            author=self.request.user,
            is_published=True,
            published_at=timezone.now()
        )

        self._send_telegram(news)

    
    def perform_update(self, serializer):
        # Обновление новости
        news = serializer.save()

    
    def perform_destroy(self, instance):
        # Удаление новости
        instance.delete()

    
    def _send_telegram(self, news):
        # Отправка новости в Telegram

        subscribers = User.objects.exclude(telegram_chat_id__isnull=True).exclude(telegram_chat_id='')

        if not subscribers.exists():
            return
        
        text = f"""{news.title}
        {news.short_description}
        Читать: https://#домен#/news/{news.id}
        """

        for user in subscribers:
            try:
                bot.send_message(user.telegram_chat_id, text)
            except Exception as e:
                print(f"Ошибка отправки {user.telegram_chat_id}: {e}")

                if "chat not found" in str(e).lower():
                    user.telegram_chat_id = None
                    user.save()


class CommentView(viewsets.ModelViewSet):
    # Класс для работы с комментариями
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Получение списка комментов к новости
        return Comment.objects.filter(
            news_id=self.kwargs.get('news_id'),
            is_deleted=False
        ).select_related('author', 'news') # Подгрузка связанных объектов (чтобы не загружать весь объект новости)
    

    def get_permissions(self):
        # Проверка прав для работы с комментариями

        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.AllowAny]

        return super().get_permissions()
    
    def create(self, serializer):
        # Создание комментария
        pass
