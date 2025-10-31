# Руководство по разработке

## Начало работы

1. **Клонирование репозитория** (когда репозиторий будет создан)
   ```bash
   git clone <repository-url>
   cd project_group_python
   ```

2. **Установка зависимостей**
   ```bash
   ./setup.sh
   ```
   Или вручную:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Настройка окружения**
   - Скопируйте `.env.example` в `.env`
   - Заполните необходимые переменные окружения

4. **Применение миграций**
   ```bash
   python manage.py migrate
   ```

5. **Создание суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запуск сервера разработки**
   ```bash
   python manage.py runserver
   ```

## Рабочий процесс (Git Flow)

1. **Создание ветки для задачи**
   ```bash
   git checkout -b feature/название-задачи
   # или
   git checkout -b fix/название-бага
   ```

2. **Коммиты**
   - Пишите понятные сообщения коммитов
   - Делайте коммиты часто, небольшими порциями
   - Формат: `[Модуль] Краткое описание изменения`

   Примеры:
   - `[News] Добавлена модель Article`
   - `[Torrents] Реализован API для загрузки торрентов`
   - `[Core] Исправлена ошибка в permissions`

3. **Push и Pull Request**
   ```bash
   git push origin feature/название-задачи
   ```
   Создайте Pull Request для code review

4. **Code Review**
   - Команда проводит review перед мержем
   - Исправьте замечания, если есть
   - После approval мержим в main

## Стандарты кода

### Python (PEP 8)
- Используйте 4 пробела для отступов
- Максимальная длина строки: 79 символов
- Используйте snake_case для функций и переменных
- Используйте PascalCase для классов
- Добавляйте docstrings для функций и классов

Пример:
```python
class NewsService:
    """
    Сервис для работы с новостями.
    """
    
    def get_news_by_category(self, category_id: int) -> QuerySet:
        """
        Получить новости по категории.
        
        Args:
            category_id: ID категории
            
        Returns:
            QuerySet новостей
        """
        return News.objects.filter(category_id=category_id)
```

### Django REST Framework
- Используйте ViewSets для CRUD операций
- Всегда используйте сериализаторы
- Правильные HTTP методы и статус коды
- Пагинация для списков

Пример:
```python
class NewsViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления новостями.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
```

### Структура кода

**Разделение ответственности**:
- `models.py` - только модели данных
- `views.py` - только обработка HTTP запросов
- `services.py` - вся бизнес-логика
- `serializers.py` - преобразование данных

**Пример правильной структуры**:

```python
# views.py
class NewsViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Используем сервис для логики
        news = NewsService.create_news(serializer.validated_data, request.user)
        return Response(NewsSerializer(news).data, status=status.HTTP_201_CREATED)

# services.py
class NewsService:
    @staticmethod
    def create_news(data, user):
        # Вся бизнес-логика здесь
        news = News.objects.create(**data, author=user)
        # Отправка уведомлений, логирование и т.д.
        return news
```

## Тестирование

### Написание тестов
- Пишите тесты для всех новых функций
- Используйте Django TestCase
- Тестируйте сервисы отдельно от views

Пример:
```python
class NewsServiceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        
    def test_create_news(self):
        data = {'title': 'Test', 'content': 'Content'}
        news = NewsService.create_news(data, self.user)
        self.assertEqual(news.title, 'Test')
```

### Запуск тестов
```bash
python manage.py test
python manage.py test apps.news  # Тесты конкретного модуля
```

## Документация

### API Документация
- Автоматическая документация доступна по адресу: `/api/docs/`
- Используйте docstrings для описания endpoints

### Комментарии
- Комментируйте сложную логику
- Объясняйте "почему", а не "что"
- Обновляйте комментарии при изменении кода

## Работа с модулями

### Распределение модулей

**Developer 1**: Core + News
- Базовая функциональность
- Модуль новостей

**Developer 2**: Torrents
- Работа с торрентами
- Интеграция libtorrent

**Developer 3**: Notifications
- Система уведомлений
- Email интеграция

### Коммуникация
- Обсуждайте изменения API перед реализацией
- Согласовывайте структуру моделей
- Информируйте команду о breaking changes

## Частые задачи

### Создание нового приложения
```bash
python manage.py startapp apps/название
```

### Создание миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Сбор статических файлов
```bash
python manage.py collectstatic
```

### Запуск Celery worker (для уведомлений)
```bash
celery -A config worker -l info
```

## Полезные ссылки

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [PEP 8 Style Guide](https://pep8.org/)

## Вопросы и помощь

Если возникли вопросы:
1. Проверьте документацию
2. Спросите у команды
3. Обратитесь к тимлиду

---

**Удачной разработки! 🚀**



