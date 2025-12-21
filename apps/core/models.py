"""
Модели базового модуля.
Здесь могут быть общие модели, расширение модели User и т.д.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Если нужна кастомная модель пользователя, раскомментируйте:
# class User(AbstractUser):
#     pass


class User(AbstractUser):
    # Модель пользователя

    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        help_text='Введите ваш email'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    
    


class Moderator(models.Model):
    # Модель модератора
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='moderator',
        verbose_name='Модератор'
    )

    can_create_news = models.BooleanField(
        verbose_name='Может создавать новости',
        default=True
    )

    can_edit_news = models.BooleanField(
        verbose_name='Может редактировать новости',
        default=True
    )
    
    
    can_delete_news = models.BooleanField(
        verbose_name='Может удалять новости',
        default=True
    )    

    can_delete_comments = models.BooleanField(
        verbose_name='Может удалять комментарии',
        default=True
    )

    can_ban_1_day = models.BooleanField(
        verbose_name='Может банить на 1 день',
        default=True
    )
    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

    def __str__(self):
        return f'Модератор {self.user.username}'
    

class AdminProfile(models.Model):
    # Модель администратора
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='admin',
        verbose_name='Админ'
    )
    
    can_ban = models.BooleanField(
        verbose_name='Может выдавать баны',
        default=True
    )
    
    can_manage_moderators = models.BooleanField(
        verbose_name='Может управлять модераторами',
        default=True
    )
    
    can_view_statistics = models.BooleanField(
        verbose_name='Может просматривать статистику',
        default=True
    )
    

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return f'Администратор {self.user.username}'