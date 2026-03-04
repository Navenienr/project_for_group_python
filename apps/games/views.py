from rest_framework import generics
from .models import Game
from .models import Genre
from .serializers import GameSerializer, GameShortSerializer, GenreSerializer

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