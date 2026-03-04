from rest_framework import generics, viewsets, permissions, status
from .models import Game, FavoriteGame
from .serializers import GameSerializer, GameShortSerializer, FavoriteGameSerializer
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameListShortView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameShortSerializer

class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_favorites(request, game_id):
    pass