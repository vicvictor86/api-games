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
    class Meta:
        model = GamePlataform
        fields = '__all__'
    
class GamePlataformView(serializers.ModelSerializer):
    """Mostra as plataformas de forma visual, mostrando o nome em vez de apenas ID da plataforma"""
    id = serializers.ReadOnlyField(source='plataform.id')
    plataform = serializers.ReadOnlyField(source='plataform.name')
    class Meta:
        model = GamePlataform
        fields = ['id', 'plataform']

class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = '__all__'

class GameGenreView(serializers.ModelSerializer):
    """Mostra os gêneros de forma visual, mostrando o nome em vez do ID do gênero"""
    id = serializers.ReadOnlyField(source='genre.id')
    genre = serializers.ReadOnlyField(source='genre.name')
    class Meta:
        model = GameGenre
        fields = ['id', 'genre']

class GameFullInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'initial_release_date', 'description', 'sales', 'price', 'image', 'studio', 'plataforms', 'genres']
    plataforms = GamePlataformView(many=True)
    genres = GameGenreView(many=True)
