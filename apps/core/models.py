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


   