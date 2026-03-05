from django.urls import path
from .views import GameListView, GameListShortView, GameDetailView, GenreListView, FavoriteGameListView
from apps.games import views as games_views

urlpatterns = [
    path('shortlist/', GameListShortView.as_view(), name='short_list'),
    path('list/', GameListView.as_view(), name='game_list'),
    path('<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('favorites/', FavoriteGameListView.as_view(), name='favorite-list'),
    path('<int:game_id>/favorite/add/', games_views.add_to_favorites, name='favorite-add'),
    path('<int:game_id>/favorite/remove/', games_views.remove_from_favorites, name='favorite-remove'),
    path('<int:game_id>/favorite/check/', games_views.check_favorite, name='favorite-check'),

]