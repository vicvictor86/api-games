from rest_framework import serializers
from games.models import *

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlataformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataform
        fields = '__all__'

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GamePlataformSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.name')
    plataform = serializers.ReadOnlyField(source='plataform.name')
    class Meta:
        model = GamePlataform
        fields = '__all__'

class GameGenreSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.name')
    genre = serializers.ReadOnlyField(source='genre.name')
    class Meta:
        model = GameGenre
        fields = '__all__'

class GameFullInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'plataforms', 'genres']
    plataforms = GamePlataformSerializer(many=True)
    genres = GameGenreSerializer(many=True)
