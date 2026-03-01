import os
import sys
import django
import time
from threading import Thread

def run_bot():
    from apps.bots.tgbot import bot

    print("Телеграм бот запущен")
    bot.infinity_polling()


if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

    run_bot()