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

    


class Moderator(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='moderator',
        verbose_name='Модератор'
    )

    can_edit = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)
    can_ban = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

        def __str__(self):
            return f'Модератор {self.user.username}'