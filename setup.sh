#!/bin/bash
# Скрипт для первоначальной настройки проекта

echo "Создание виртуального окружения..."
python3 -m venv venv

echo "Активация виртуального окружения..."
source venv/bin/activate

echo "Установка зависимостей..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Создание .env файла из примера..."
if [ ! -f .env ]; then
    cp .env.example .env 2>/dev/null || echo "Создайте .env файл вручную на основе .env.example"
fi

echo "Применение миграций..."
python manage.py migrate

echo "Создание суперпользователя..."
echo "Выполните: python manage.py createsuperuser"

echo "Сбор статических файлов..."
python manage.py collectstatic --noinput

echo "Готово! Для запуска сервера выполните:"
echo "  python manage.py runserver"



