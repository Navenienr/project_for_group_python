"""
Модели модуля уведомлений.
"""
from django.db import models
from django.conf import settings
from django.utils import timezone


class NotificationType(models.Model):
    """Тип уведомления"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название типа'
    )
    
    code = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Код типа',
        help_text='Уникальный код для программного использования'
    )
    
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    
    email_template = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Шаблон email',
        help_text='Путь к шаблону email уведомления'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )

    class Meta:
        verbose_name = 'Тип уведомления'
        verbose_name_plural = 'Типы уведомлений'

    def __str__(self):
        return self.name


class NotificationSettings(models.Model):
    """Настройки подписок пользователя на уведомления"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notification_settings',
        verbose_name='Пользователь'
    )
    
    email_enabled = models.BooleanField(
        default=True,
        verbose_name='Email уведомления включены'
    )
    
    new_news_enabled = models.BooleanField(
        default=True,
        verbose_name='Уведомления о новых новостях'
    )
    
    new_comments_enabled = models.BooleanField(
        default=True,
        verbose_name='Уведомления о новых комментариях'
    )
    
    torrent_updates_enabled = models.BooleanField(
        default=True,
        verbose_name='Уведомления об обновлениях торрентов'
    )
    
    moderation_enabled = models.BooleanField(
        default=False,
        verbose_name='Уведомления о модерации',
        help_text='Только для модераторов и администраторов'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Настройки уведомлений'
        verbose_name_plural = 'Настройки уведомлений'

    def __str__(self):
        return f'Настройки уведомлений для {self.user.username}'


class Notification(models.Model):
    """История уведомлений"""
    STATUS_CHOICES = [
        ('pending', 'Ожидает отправки'),
        ('sent', 'Отправлено'),
        ('read', 'Прочитано'),
        ('failed', 'Ошибка отправки'),
    ]
    
    TYPE_CHOICES = [
        ('new_news', 'Новая новость'),
        ('new_comment', 'Новый комментарий'),
        ('torrent_update', 'Обновление торрента'),
        ('moderation', 'Модерация'),
        ('system', 'Системное'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name='Пользователь'
    )
    
    notification_type = models.ForeignKey(
        NotificationType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications',
        verbose_name='Тип уведомления'
    )
    
    type_code = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        verbose_name='Код типа',
        help_text='Тип уведомления для быстрого доступа'
    )
    
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    
    message = models.TextField(
        verbose_name='Сообщение'
    )
    
    link = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка',
        help_text='Ссылка для перехода при клике на уведомление'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    
    email_sent = models.BooleanField(
        default=False,
        verbose_name='Email отправлен'
    )
    
    email_sent_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата отправки email'
    )
    
    read_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата прочтения'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    # Связи с другими моделями для контекста
    related_news = models.ForeignKey(
        'news.News',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications',
        verbose_name='Связанная новость'
    )
    
    related_torrent = models.ForeignKey(
        'torrents.TorrentFile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications',
        verbose_name='Связанный торрент'
    )

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['status']),
            models.Index(fields=['type_code']),
        ]

    def __str__(self):
        return f'{self.title} для {self.user.username}'
    
    def mark_as_read(self):
        """Отметить уведомление как прочитанное"""
        if not self.read_at:
            self.status = 'read'
            self.read_at = timezone.now()
            self.save(update_fields=['status', 'read_at'])
    
    def mark_as_sent(self):
        """Отметить уведомление как отправленное"""
        self.status = 'sent'
        self.email_sent = True
        self.email_sent_at = timezone.now()
        self.save(update_fields=['status', 'email_sent', 'email_sent_at'])


class NotificationSubscription(models.Model):
    """Подписки пользователей на определенные типы уведомлений"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Пользователь'
    )
    
    notification_type = models.ForeignKey(
        NotificationType,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Тип уведомления'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подписки'
    )

    class Meta:
        verbose_name = 'Подписка на уведомления'
        verbose_name_plural = 'Подписки на уведомления'
        unique_together = ['user', 'notification_type']
        indexes = [
            models.Index(fields=['user', 'is_active']),
        ]

    def __str__(self):
        return f'{self.user.username} подписан на {self.notification_type.name}'
