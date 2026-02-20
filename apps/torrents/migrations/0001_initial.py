# Generated migration for torrents app

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.db.models import Q


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TorrentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название торрента')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('torrent_file', models.FileField(upload_to='torrents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['torrent'])], verbose_name='Торрент-файл')),
                ('file_size', models.BigIntegerField(help_text='Размер файла в байтах', verbose_name='Размер файла (байты)')),
                ('file_size_mb', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Размер файла (МБ)')),
                ('seeders', models.PositiveIntegerField(default=0, help_text='Количество раздающих', verbose_name='Сидеры')),
                ('leechers', models.PositiveIntegerField(default=0, help_text='Количество скачивающих', verbose_name='Личеры')),
                ('download_count', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний')),
                ('status', models.CharField(choices=[('pending', 'Ожидает загрузки'), ('downloading', 'Загружается'), ('completed', 'Завершено'), ('paused', 'Приостановлено'), ('error', 'Ошибка')], default='pending', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('news', models.ForeignKey(help_text='Новость, к которой прикреплен торрент', on_delete=django.db.models.deletion.CASCADE, related_name='torrents', to='news.news', verbose_name='Связанная новость')),
                ('uploaded_by', models.ForeignKey(limit_choices_to=Q(('is_moderator', True), ('is_superuser', True), _connector='OR'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploaded_torrents', to=settings.AUTH_USER_MODEL, verbose_name='Загрузил')),
            ],
            options={
                'verbose_name': 'Торрент-файл',
                'verbose_name_plural': 'Торрент-файлы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TorrentDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('downloading', 'Загружается'), ('completed', 'Завершено'), ('paused', 'Приостановлено'), ('cancelled', 'Отменено'), ('error', 'Ошибка')], default='downloading', max_length=20, verbose_name='Статус загрузки')),
                ('progress', models.DecimalField(decimal_places=2, default=0.0, help_text='Процент загрузки от 0 до 100', max_digits=5, verbose_name='Прогресс (%)')),
                ('downloaded_bytes', models.BigIntegerField(default=0, verbose_name='Загружено (байты)')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Начало загрузки')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Завершение загрузки')),
                ('error_message', models.TextField(blank=True, verbose_name='Сообщение об ошибке')),
                ('torrent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloads', to='torrents.torrentfile', verbose_name='Торрент')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torrent_downloads', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Загрузка торрента',
                'verbose_name_plural': 'Загрузки торрентов',
            },
        ),
        migrations.AddIndex(
            model_name='torrentfile',
            index=models.Index(fields=['-created_at'], name='torrents_to_created_idx'),
        ),
        migrations.AddIndex(
            model_name='torrentfile',
            index=models.Index(fields=['status'], name='torrents_to_status_idx'),
        ),
        migrations.AddIndex(
            model_name='torrentfile',
            index=models.Index(fields=['news'], name='torrents_to_news_idx'),
        ),
        migrations.AddIndex(
            model_name='torrentdownload',
            index=models.Index(fields=['user', '-started_at'], name='torrents_to_user_started_idx'),
        ),
        migrations.AddIndex(
            model_name='torrentdownload',
            index=models.Index(fields=['torrent', 'status'], name='torrents_to_torrent_status_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='torrentdownload',
            unique_together={('torrent', 'user')},
        ),
    ]
