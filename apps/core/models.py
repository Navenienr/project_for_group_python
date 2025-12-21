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
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='пользователь'
        null=True,
        blank=True
    )
    
