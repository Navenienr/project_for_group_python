# Generated migration for notifications app

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('torrents', '0001_initial'),
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название типа')),
                ('code', models.SlugField(help_text='Уникальный код для программного использования', max_length=50, unique=True, verbose_name='Код типа')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('email_template', models.CharField(blank=True, help_text='Путь к шаблону email уведомления', max_length=200, verbose_name='Шаблон email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Тип уведомления',
                'verbose_name_plural': 'Типы уведомлений',
            },
        ),
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_enabled', models.BooleanField(default=True, verbose_name='Email уведомления включены')),
                ('new_news_enabled', models.BooleanField(default=True, verbose_name='Уведомления о новых новостях')),
                ('new_comments_enabled', models.BooleanField(default=True, verbose_name='Уведомления о новых комментариях')),
                ('torrent_updates_enabled', models.BooleanField(default=True, verbose_name='Уведомления об обновлениях торрентов')),
                ('moderation_enabled', models.BooleanField(default=False, help_text='Только для модераторов и администраторов', verbose_name='Уведомления о модерации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notification_settings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Настройки уведомлений',
                'verbose_name_plural': 'Настройки уведомлений',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_code', models.CharField(choices=[('new_news', 'Новая новость'), ('new_comment', 'Новый комментарий'), ('torrent_update', 'Обновление торрента'), ('moderation', 'Модерация'), ('system', 'Системное')], help_text='Тип уведомления для быстрого доступа', max_length=50, verbose_name='Код типа')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('link', models.URLField(blank=True, help_text='Ссылка для перехода при клике на уведомление', null=True, verbose_name='Ссылка')),
                ('status', models.CharField(choices=[('pending', 'Ожидает отправки'), ('sent', 'Отправлено'), ('read', 'Прочитано'), ('failed', 'Ошибка отправки')], default='pending', max_length=20, verbose_name='Статус')),
                ('email_sent', models.BooleanField(default=False, verbose_name='Email отправлен')),
                ('email_sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки email')),
                ('read_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата прочтения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('notification_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='notifications.notificationtype', verbose_name='Тип уведомления')),
                ('related_news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='news.news', verbose_name='Связанная новость')),
                ('related_torrent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='torrents.torrentfile', verbose_name='Связанный торрент')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NotificationSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')),
                ('notification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='notifications.notificationtype', verbose_name='Тип уведомления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка на уведомления',
                'verbose_name_plural': 'Подписки на уведомления',
            },
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['user', '-created_at'], name='notificatio_user_created_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['status'], name='notificatio_status_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['type_code'], name='notificatio_type_code_idx'),
        ),
        migrations.AddIndex(
            model_name='notificationsubscription',
            index=models.Index(fields=['user', 'is_active'], name='notificatio_user_is_active_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='notificationsubscription',
            unique_together={('user', 'notification_type')},
        ),
    ]
