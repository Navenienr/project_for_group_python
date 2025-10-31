"""
URL маршруты модуля уведомлений.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'notifications'

router = DefaultRouter()
# router.register(r'notifications', views.NotificationViewSet)
# router.register(r'subscriptions', views.SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



