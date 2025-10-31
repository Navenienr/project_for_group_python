"""
URL маршруты модуля новостей.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'news'

router = DefaultRouter()
# router.register(r'articles', views.ArticleViewSet)
# router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



