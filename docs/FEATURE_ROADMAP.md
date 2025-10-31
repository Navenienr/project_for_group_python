# Roadmap дополнительных функций

## 🔥 Приоритет 1: Критически важные (MVP+)

### 1. Аутентификация и Авторизация

**Модуль**: Создать `apps/auth/` или расширить `apps/core/`

**Зависимости**:
```python
# Уже есть в requirements.txt
djangorestframework-simplejwt==5.3.0
```

**Структура**:
```
apps/auth/
├── models.py          # User profile расширение
├── serializers.py     # Register, Login, Profile serializers
├── views.py           # Auth viewsets
├── urls.py            # Auth routes
├── permissions.py    # Role-based permissions
└── services.py        # Auth business logic
```

**Основные функции**:
- JWT токены (access + refresh)
- Регистрация с email подтверждением
- Восстановление пароля
- Профиль пользователя
- Роли: Admin, Moderator, User

**Оценка времени**: 2-3 дня

---

### 2. Система рейтингов и взаимодействия

**Модуль**: Расширить `apps/news/`

**Новые модели**:
```python
class Like(models.Model):
    user = ForeignKey(User)
    news = ForeignKey(News)
    liked_at = DateTimeField
    
class Favorite(models.Model):
    user = ForeignKey(User)
    news = ForeignKey(News)
    
class NewsRating(models.Model):
    user = ForeignKey(User)
    news = ForeignKey(News)
    rating = IntegerField(1-5)
    
class ViewHistory(models.Model):
    user = ForeignKey(User)
    news = ForeignKey(News)
    viewed_at = DateTimeField
```

**API Endpoints**:
- `POST /api/news/{id}/like/`
- `GET /api/news/trending/` - по количеству лайков
- `GET /api/news/favorites/` - избранное пользователя

**Оценка времени**: 2 дня

---

### 3. Расширенный поиск

**Технология**: Django PostgreSQL full-text search или Django-Haystack (для SQLite можно использовать простой поиск)

**Зависимости** (опционально):
```python
# Для полнотекстового поиска с PostgreSQL
django-extensions==3.2.3

# Или для простого поиска (работает с SQLite)
# Дополнительных зависимостей не требуется
```

**Реализация**:
- Простой поиск: `News.objects.filter(title__icontains=query)`
- Расширенный: фильтрация по дате, категории, автору
- Автокомплит через API

**Оценка времени**: 1-2 дня

---

## 🎯 Приоритет 2: Рекомендуемые функции

### 4. Комментарии с threading

**Модуль**: Расширить `apps/news/`

**Модель комментариев**:
```python
class Comment(models.Model):
    news = ForeignKey(News)
    user = ForeignKey(User)
    parent = ForeignKey('self', null=True)  # Для вложенности
    content = TextField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    likes_count = IntegerField(default=0)
```

**API**:
- Вложенные комментарии (tree structure)
- Лайки на комментарии
- Редактирование

**Оценка времени**: 2-3 дня

---

### 5. Теги и категоризация

**Модуль**: Расширить `apps/news/`

**Модель**:
```python
class Tag(models.Model):
    name = CharField(unique=True)
    slug = SlugField()
    
class NewsTag(models.Model):
    news = ForeignKey(News)
    tag = ForeignKey(Tag)
```

**Функции**:
- Облако тегов
- Фильтрация по тегам
- Подписки на теги

**Оценка времени**: 1-2 дня

---

### 6. Расширенная работа с торрентами

**Модуль**: Расширить `apps/torrents/`

**Новые функции**:
- Категории торрентов
- Рейтинги
- Комментарии
- Очередь загрузок
- Ограничение скорости
- Автопауза при достижении лимита трафика

**Оценка времени**: 3-4 дня

---

### 7. Аналитика

**Модуль**: Новый `apps/analytics/`

**Функции**:
- Популярные новости
- Статистика просмотров
- Статистика загрузок
- Аналитика для админов

**Технология**: Aggregation queries Django ORM

**Оценка времени**: 2 дня

---

## 📦 Дополнительные зависимости

Обновленный `requirements.txt` (дополнительно):

```python
# Для email верификации
django-allauth==0.54.0  # Опционально, можно обойтись своими решениями

# Для полнотекстового поиска (если будет PostgreSQL)
django-extensions==3.2.3

# Для работы с изображениями
Pillow==10.1.0

# Для генерации PDF (если нужно)
reportlab==4.0.7

# Для RSS фидов
django-feeds==2.0.0  # Или своя реализация

# Для кеширования (Redis уже есть)
# redis==5.0.1  # Уже в requirements.txt
django-redis==5.3.0  # Для удобной работы с Redis кешем

# Для WebSocket (если планируется)
channels==4.0.0
channels-redis==4.1.0

# Для мониторинга
django-debug-toolbar==4.2.0  # Только для development
```

---

## План реализации по неделям

### Неделя 1-2: MVP
- ✅ Структура проекта (готово)
- ⚠️ Аутентификация
- ⚠️ Базовый CRUD новостей
- ⚠️ Базовый CRUD торрентов
- ⚠️ Простые уведомления

### Неделя 3: Core Features
- Рейтинги и лайки
- Комментарии
- Профили пользователей

### Неделя 4: Enhancement
- Поиск и фильтрация
- Теги
- Расширенные функции торрентов

### Неделя 5-6: Polish
- Аналитика
- Оптимизация
- Тестирование
- Документация

---

## Рекомендации по распределению задач

### Вариант 1: По модулям
- **Developer 1**: Auth + News + Ratings
- **Developer 2**: Torrents (базовый + расширенный)
- **Developer 3**: Notifications + Analytics + Search

### Вариант 2: По функциональности
- **Developer 1**: Auth + User profiles + Ratings
- **Developer 2**: News (CRUD + Comments + Tags + Search)
- **Developer 3**: Torrents + Notifications + Analytics

### Вариант 3: Гибридный (рекомендуется)
- **Developer 1**: Core/Auth + News базовый + Ratings/Comments
- **Developer 2**: Torrents полный цикл
- **Developer 3**: Notifications + Analytics + Search/Filter
- **Team Lead**: Интеграция, Code Review, Testing

---

## Метрики успеха проекта

✅ **MVP считается готовым когда**:
- Пользователи могут регистрироваться и входить
- Админы могут создавать новости
- Пользователи могут просматривать новости
- Торренты можно загружать и управлять ими
- Уведомления работают

✅ **Проект считается успешным когда**:
- Все модули интегрированы
- Есть система рейтингов
- Работает поиск
- Есть тесты (покрытие >60%)
- Документация API готова
- Frontend интегрирован (если используется)

---

## Потенциальные проблемы и решения

### Проблема 1: SQLite ограничения
**Решение**: 
- Для MVP SQLite достаточно
- Если понадобится, легко мигрировать на PostgreSQL
- SQLite отлично для разработки и небольших проектов

### Проблема 2: Сложность libtorrent
**Решение**:
- Использовать готовые обертки
- Начать с простой реализации
- Добавлять функции постепенно

### Проблема 3: Асинхронные задачи (Celery)
**Решение**:
- Начать с синхронной отправки email
- Добавить Celery позже
- Redis можно заменить на локальный брокер для разработки

### Проблема 4: Координация команды
**Решение**:
- Четкое разделение модулей
- Регулярные код-ревью
- Обсуждение API перед реализацией
- Документация интерфейсов между модулями



