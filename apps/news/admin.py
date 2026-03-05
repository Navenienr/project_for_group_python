from django.contrib import admin
from .models import News, Comment
from django.contrib.auth import get_user_model
import telebot
from django.conf import settings
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at']

    def save_model(self, request, obj, form, change):
        # Сохранять новость через API для тг бота
        super().save_model(request, obj, form, change)

        if not change and obj.is_published:
            self._send_telegram_notification(obj)

    def _send_telegram_notification(self, news):
        # Отправка новости в телеграм
        User = get_user_model()
        bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

        subscribers = User.objects.exclude(telegram_chat_id__isnull=True)

        if not subscribers.exists():
            return

        text = f"""{news.title}
        {news.short_description}
        Читать: https://127.0.0.1:8000/news/{news.id}
        """

        for user in subscribers:
            try:
                bot.send_message(user.telegram_chat_id, text)
            except Exception as e:
                print(f"Ошибка отправки {user.telegram_chat_id}: {e}")

                if "chat not found" in str(e).lower():
                    user.telegram_chat_id = None
                    user.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'author', 'created_at', 'is_deleted','short_content']

    list_filter = ['is_deleted', 'created_at']

    def short_content(self, obj):
        return obj.content[:100]

    short_content.short_description = 'Комментарий'