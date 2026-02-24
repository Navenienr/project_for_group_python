"""
Представления модуля новостей.
"""
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import News
from .serializers import NewsSerializer
import telebot
from django.conf import settings


User = get_user_model()

TOKEN = '8733942341:AAGEpWvQnvvkMfaLLcO31TVRQ57RkpFj3cA'

bot = telebot.TeleBot(TOKEN)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        news = serializer.save()

        users = User.objects.filter(telegram_chat_id__isnull=False)

        for user in users:
            try:
                bot.send_message(
                    user.telegram_chat_id,
                    f"📰 Новая новость!\n\n{news.title}"
                )
            except Exception as e:
                print(f"Ошибка отправки {user.telegram_chat_id}: {e}")
