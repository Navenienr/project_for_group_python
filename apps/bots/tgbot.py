from django.utils import timezone
import time
from django.db import close_old_connections
import asyncio
from telegram import Bot
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.news.models import News
from apps.core.models import User


TOKEN = '8733942341:AAGEpWvQnvvkMfaLLcO31TVRQ57RkpFj3cA'

bot = Bot(token=TOKEN)


queue = []

last_check = timezone.now()


async def send_news(news):
    close_old_connections()

    # Рассылка новостей всем пользователям (у которых есть тг username)
    users = User.objects.filter(
        tg_username__isnull=False).exclude(tg_username='')

    if not users:
        print('Нет пользователей с тг username')
        return

    text = f"""
{news.title}
{news.content[:200]}...
Ссылка: https://gamesite.ru/news/{news.id}
    """

    for user in users:
        try:
            await bot.send_message(chat_id=f"@{user.tg_username}", text=text)
        except Exception as e:
            print(f"Ошибка @{user.tg_username}: {e}")

    print(f"Рассылка новости {news.id} завершена")


def check_for_new_news():
    global last_check
    # Проверка на новые новости
    new_news = News.objects.filter(
        created_at__gt=last_check,
        is_published=True
    )

    for news in new_news:
        if news.id not in queue:
            queue.append(news.id)


    last_check = timezone.now()


def sent_from_queue():
    check_for_new_news()

    while True:
        if queue:
            news_id = queue.pop(0)
            try:
                news = News.objects.get(id=news_id)
                if news:
                    asyncio.run(send_news(news))
            except News.DoesNotExist:
                print(f"Новость {news_id} не найдена")
            except Exception as e:
                print(f"Ошибка: {e}")

            time.sleep(120)
        else:
            time.sleep(300)
            check_for_new_news()


if __name__ == "__main__":
    sent_from_queue()
