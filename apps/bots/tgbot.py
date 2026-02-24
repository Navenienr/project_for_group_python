import asyncio
from telegram import Bot
from apps.core.models import User
from apps.news.models import News
import time
from django.utils import timezone


TOKEN = '8553032782:AAEGpLhH8kZWIEWIvEPd1PL6kNBwOU-sLU4'

bot = Bot(token=TOKEN)


queue = []

last_check = timezone.now()


async def send_news(news):
    # Рассылка новостей всем пользователям (у которых есть тг ID)
    users = User.objects.filter(tg_username_id__isnull=False).exclude(tg_username_id='')

    if not users:
        print('Нет пользователей с тг ID')
        return
    
    text = f"""
    {news.title}
    {news.content[:200]}...
    Ссылка: https://#домен#/news/{news.id}
    """ # Ссылку нужно доработать
    

    for user in users:
        try:
            await bot.send_message(chat_id=user.tg_username_id, text=text)
        except Exception as e:
            print(e)
        
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
            except Exception as e:
                print(e)
            
            time.sleep(120)
        else:
            time.sleep(300)
            check_for_new_news()