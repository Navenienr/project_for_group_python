from django.contrib.auth import get_user_model
import os
import django
import telebot

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


User = get_user_model()

TOKEN = "8733942341:AAGEpWvQnvvkMfaLLcO31TVRQ57RkpFj3cA"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id

    # создаём "виртуального" пользователя
    user, created = User.objects.get_or_create(
        username=f"tg_{chat_id}",
        defaults={
            "email": f"tg_{chat_id}@telegram.com"
        }
    )

    user.telegram_chat_id = chat_id
    user.save()

    bot.send_message(chat_id, "✅ Вы подписались на новости!")


if __name__ == "__main__":
    bot.infinity_polling()
