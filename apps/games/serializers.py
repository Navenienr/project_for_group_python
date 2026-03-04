from rest_framework import serializers
from .models import Game, Genre, Language

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    interface_language = LanguageSerializer(many=True, read_only=True)
    voice_language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            'id', 'name', 'genres', 'version', 'developer', 'download_link',
            'interface_language', 'voice_language', 'release_date',
            'min_requirements', 'rec_requirements', 'description', 'created_at'
        ]

class GameShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'genres'] 

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']