"""
Модели модуля новостей.
"""
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Category(models.Model):
    """Категория новостей"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='URL-адрес'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    """Модель новостей"""
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
        validators=[MinLengthValidator(5)]
    )
    
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL-адрес',
        help_text='Автоматически генерируется из заголовка'
    )
    
    content = models.TextField(
        verbose_name='Содержание',
        validators=[MinLengthValidator(50)]
    )
    
    short_description = models.CharField(
        max_length=300,
        verbose_name='Краткое описание',
        help_text='Краткое описание для превью новости'
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='news',
        verbose_name='Автор',
        limit_choices_to=models.Q(is_moderator=True) | models.Q(is_superuser=True)
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='news',
        verbose_name='Категория'
    )
    
    image = models.ImageField(
        upload_to='news_images/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров'
    )
    
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True
    )
    
    published_at = models.DateTimeField(
        verbose_name='Дата публикации',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['category']),
            models.Index(fields=['is_published']),
        ]
        permissions = [
            ('can_create_news', 'Может создавать новости'),
            ('can_edit_news', 'Может редактировать новости'),
            ('can_delete_news', 'Может удалять новости'),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def can_edit(self, user):
        """Проверка, может ли пользователь редактировать новость"""
        if user.is_superuser:
            return True
        if user.is_moderator and user.can_edit_news:
            return True
        return False

    def can_delete(self, user):
        """Проверка, может ли пользователь удалять новость"""
        if user.is_superuser:
            return True
        if user.is_moderator and user.can_delete_news:
            return True
        return False
    
    def increment_views(self):
        """Увеличить счетчик просмотров"""
        self.views_count += 1
        self.save(update_fields=['views_count'])


class Comment(models.Model):
    """Комментарий к новости с поддержкой threading (ответы на комментарии)"""
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Новость'
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name='Родительский комментарий',
        help_text='Если это ответ на другой комментарий'
    )
    
    content = models.TextField(
        verbose_name='Содержание комментария',
        validators=[MinLengthValidator(3)]
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    is_edited = models.BooleanField(
        default=False,
        verbose_name='Отредактирован'
    )
    
    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Удален'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['news', '-created_at']),
            models.Index(fields=['parent']),
        ]

    def __str__(self):
        return f'Комментарий от {self.author.username} к новости "{self.news.title[:30]}"'
    
    def get_replies_count(self):
        """Получить количество ответов на комментарий"""
        return self.replies.filter(is_deleted=False).count()


class NewsLike(models.Model):
    """Лайк новости"""
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Новость'
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='news_likes',
        verbose_name='Пользователь'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Лайк новости'
        verbose_name_plural = 'Лайки новостей'
        unique_together = ['news', 'user']
        indexes = [
            models.Index(fields=['news', 'user']),
        ]

    def __str__(self):
        return f'{self.user.username} лайкнул "{self.news.title[:30]}"'


class NewsFavorite(models.Model):
    """Избранное (добавление новости в избранное)"""
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Новость'
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorite_news',
        verbose_name='Пользователь'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        verbose_name = 'Избранная новость'
        verbose_name_plural = 'Избранные новости'
        unique_together = ['news', 'user']
        indexes = [
            models.Index(fields=['user', '-created_at']),
        ]

    def __str__(self):
        return f'{self.user.username} добавил в избранное "{self.news.title[:30]}"'
