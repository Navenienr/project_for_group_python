"""
Модели модуля торрентов.
"""
from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


class TorrentFile(models.Model):
    """Торрент-файл"""
    STATUS_CHOICES = [
        ('pending', 'Ожидает загрузки'),
        ('downloading', 'Загружается'),
        ('completed', 'Завершено'),
        ('paused', 'Приостановлено'),
        ('error', 'Ошибка'),
    ]
    
    news = models.ForeignKey(
        'news.News',
        on_delete=models.CASCADE,
        related_name='torrents',
        verbose_name='Связанная новость',
        help_text='Новость, к которой прикреплен торрент'
    )
    
    title = models.CharField(
        max_length=200,
        verbose_name='Название торрента'
    )
    
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    
    torrent_file = models.FileField(
        upload_to='torrents/',
        verbose_name='Торрент-файл',
        validators=[FileExtensionValidator(allowed_extensions=['torrent'])]
    )
    
    file_size = models.BigIntegerField(
        verbose_name='Размер файла (байты)',
        help_text='Размер файла в байтах'
    )
    
    file_size_mb = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Размер файла (МБ)',
        editable=False
    )
    
    seeders = models.PositiveIntegerField(
        default=0,
        verbose_name='Сидеры',
        help_text='Количество раздающих'
    )
    
    leechers = models.PositiveIntegerField(
        default=0,
        verbose_name='Личеры',
        help_text='Количество скачивающих'
    )
    
    download_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество скачиваний'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='uploaded_torrents',
        verbose_name='Загрузил',
        limit_choices_to=models.Q(is_moderator=True) | models.Q(is_superuser=True)
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )

    class Meta:
        verbose_name = 'Торрент-файл'
        verbose_name_plural = 'Торрент-файлы'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
            models.Index(fields=['news']),
        ]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Автоматически вычислять размер в МБ"""
        if self.file_size:
            self.file_size_mb = self.file_size / (1024 * 1024)
        super().save(*args, **kwargs)
    
    def increment_download(self):
        """Увеличить счетчик скачиваний"""
        self.download_count += 1
        self.save(update_fields=['download_count'])


class TorrentDownload(models.Model):
    """Статистика загрузок торрентов пользователями"""
    STATUS_CHOICES = [
        ('downloading', 'Загружается'),
        ('completed', 'Завершено'),
        ('paused', 'Приостановлено'),
        ('cancelled', 'Отменено'),
        ('error', 'Ошибка'),
    ]
    
    torrent = models.ForeignKey(
        TorrentFile,
        on_delete=models.CASCADE,
        related_name='downloads',
        verbose_name='Торрент'
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='torrent_downloads',
        verbose_name='Пользователь'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='downloading',
        verbose_name='Статус загрузки'
    )
    
    progress = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        verbose_name='Прогресс (%)',
        help_text='Процент загрузки от 0 до 100'
    )
    
    downloaded_bytes = models.BigIntegerField(
        default=0,
        verbose_name='Загружено (байты)'
    )
    
    started_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Начало загрузки'
    )
    
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Завершение загрузки'
    )
    
    error_message = models.TextField(
        blank=True,
        verbose_name='Сообщение об ошибке'
    )

    class Meta:
        verbose_name = 'Загрузка торрента'
        verbose_name_plural = 'Загрузки торрентов'
        unique_together = ['torrent', 'user']
        indexes = [
            models.Index(fields=['user', '-started_at']),
            models.Index(fields=['torrent', 'status']),
        ]

    def __str__(self):
        return f'{self.user.username} - {self.torrent.title} ({self.get_status_display()})'
    
    def complete_download(self):
        """Завершить загрузку"""
        from django.utils import timezone
        self.status = 'completed'
        self.progress = 100.00
        self.completed_at = timezone.now()
        self.save()
        self.torrent.increment_download()
