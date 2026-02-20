# Generated migration for news app

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.db.models import Q


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL-адрес')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Заголовок')),
                ('slug', models.SlugField(help_text='Автоматически генерируется из заголовка', max_length=200, unique=True, verbose_name='URL-адрес')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(50)], verbose_name='Содержание')),
                ('short_description', models.CharField(help_text='Краткое описание для превью новости', max_length=300, verbose_name='Краткое описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Изображение')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(limit_choices_to=Q(('is_moderator', True), ('is_superuser', True), _connector='OR'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='news.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
                'permissions': [('can_create_news', 'Может создавать новости'), ('can_edit_news', 'Может редактировать новости'), ('can_delete_news', 'Может удалять новости')],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Содержание комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_edited', models.BooleanField(default=False, verbose_name='Отредактирован')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.news', verbose_name='Новость')),
                ('parent', models.ForeignKey(blank=True, help_text='Если это ответ на другой комментарий', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='news.comment', verbose_name='Родительский комментарий')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewsLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='news.news', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_likes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Лайк новости',
                'verbose_name_plural': 'Лайки новостей',
            },
        ),
        migrations.CreateModel(
            name='NewsFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='news.news', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_news', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранная новость',
                'verbose_name_plural': 'Избранные новости',
            },
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['-created_at'], name='news_news_created_idx'),
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['category'], name='news_news_category_idx'),
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['is_published'], name='news_news_is_publ_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['news', '-created_at'], name='news_comment_news_created_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['parent'], name='news_comment_parent_idx'),
        ),
        migrations.AddIndex(
            model_name='newslike',
            index=models.Index(fields=['news', 'user'], name='news_newslik_news_user_idx'),
        ),
        migrations.AddIndex(
            model_name='newsfavorite',
            index=models.Index(fields=['user', '-created_at'], name='news_newsfav_user_created_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='newslike',
            unique_together={('news', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='newsfavorite',
            unique_together={('news', 'user')},
        ),
    ]
