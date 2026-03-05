"""
URL маршруты модуля новостей.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'news'

router = DefaultRouter()
router.register(r'news', views.NewsViewSet, basename='news')
# router.register(r'articles', views.ArticleViewSet)
# router.register(r'categories', views.CategoryViewSet)



urlpatterns = [
    path('', include(router.urls)),
    # Ручная привязка комментариев
    # path('news/<int:news_pk>/comments/', views.CommentView.as_view({'get': 'list', 'post': 'create'})),
    # path('news/<int:news_pk>/comments/<int:pk>/', views.CommentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
