from rest_framework import generics, viewsets, permissions, status
from .models import Game, Genre, FavoriteGame
from .serializers import GameSerializer, GameShortSerializer,GenreSerializer, FavoriteGameSerializer
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameListShortView(generics.ListAPIView):
    serializer_class = GameShortSerializer
    def get_queryset(self):
        queryset = Game.objects.all()
        genre_id = self.request.query_params.get('genre')
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)
        return queryset

class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    pagination_class = None

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_favorites(request, game_id):
    pass
