from apps.core.models import User
from apps.news.models import News, Category
from apps.bots import tgbot
import os
import django
import asyncio
from datetime import datetime
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


# ⚠️ ВСТАВЬ СВОЙ ЧИСЛОВОЙ ID (узнай у @userinfobot)
MY_TELEGRAM_ID = 123456789  # 👈 СЮДА ЦИФРЫ

print("🚀 ТЕСТ ДЛЯ @z3kanya")
print("=" * 60)

try:
    # Очищаем всё
    print("1️⃣ Очистка базы...")
    News.objects.all().delete()
    Category.objects.all().delete()
    User.objects.all().delete()
    print("   ✅ База пуста")

    # Создаем тебя (с числовым ID)
    print("\n2️⃣ Добавляем @z3kanya в базу...")
    user = User.objects.create(
        username="z3kanya",
        tg_username_id=MY_TELEGRAM_ID,  # Сюда ЧИСЛО
        email="z3kanya@telegram.local"
    )
    print(f"   ✅ Пользователь создан: {user.username}")
    print(f"   ✅ Telegram ID: {user.tg_username_id} (число)")

    # Создаем категорию
    print("\n3️⃣ Создаем категорию...")
    category = Category.objects.create(name="Тест")

    # Создаем новость
    print("\n4️⃣ Создаем новость...")
    news = News.objects.create(
        title=f"Привет, @z3kanya! {datetime.now().strftime('%H:%M')}",
        content="Это тест бота. Если читаешь - всё работает!",
        category=category,
        is_published=True
    )

    # Добавляем в очередь и отправляем
    print("\n5️⃣ Проверяем очередь...")
    bot.queue = []
    bot.last_check = timezone.now() - timezone.timedelta(minutes=10)
    bot.check_for_new_news()

    if bot.queue:
        news_id = bot.queue.pop(0)
        news_obj = News.objects.get(id=news_id)
        print("   📨 Отправляем...")
        asyncio.run(bot.send_news(news_obj))
        print("   ✅ Отправлено!")
    else:
        print("   ❌ Ошибка: новость не в очереди")

    print("\n" + "=" * 60)
    print("📱 @z3kanya, проверь Telegram!")
    print("=" * 60)

finally:
    # Очищаем
    print("\n🧹 Очистка...")
    News.objects.all().delete()
    Category.objects.all().delete()
    User.objects.all().delete()
    bot.queue = []
    print("✅ Всё удалено")
