"""
URL маршруты модуля торрентов.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'torrents'

router = DefaultRouter()
# router.register(r'torrents', views.TorrentViewSet)
# router.register(r'downloads', views.DownloadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



