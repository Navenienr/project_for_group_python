from django.urls import path
from .views import GameListView, GameListShortView, GameDetailView

urlpatterns = [
    path('shortlist/', GameListShortView.as_view(), name='short_list'),
    path('list/', GameListView.as_view(), name='game_list'),
    path('<int:pk>/', GameDetailView.as_view(), name='game_detail'),

]