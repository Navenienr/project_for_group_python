import asyncio
from telegram import Bot
from apps.core.models import User
from apps.news.models import News


TOKEN = ''

bot = Bot(token=TOKEN)

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

if __name__ == '__main__':
    news = News.objects.first()
    if news:
        asyncio.run(send_news(news))