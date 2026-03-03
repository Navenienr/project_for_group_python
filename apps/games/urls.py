from django.urls import path
from .views import GameListView, GameListShortView

urlpatterns = [
    path('list/', GameListShortView.as_view(), name='game-list'),
]