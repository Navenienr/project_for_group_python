from rest_framework import generics
from .models import Game
from .serializers import GameSerializer, GameShortSerializer

class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameListShortView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameShortSerializer

class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer