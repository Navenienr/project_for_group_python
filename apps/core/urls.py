"""
URL маршруты базового модуля.
"""
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('health/', views.health_check, name='health-check'),
    path('register/', views.RegisterView.as_view(), name='register'),
]



