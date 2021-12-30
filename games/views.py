from rest_framework import viewsets, generics
from games.models import *
from games.serializer import *
from django.db.models import Q

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    def get_queryset(self):
        queryset = Game.objects.all()
        game_price = self.request.query_params.get('price')
        print(game_price)
        if game_price is not None:
            
            queryset = queryset.filter(price=game_price)
        return queryset

class PlataformViewSet(viewsets.ModelViewSet):
    queryset = Plataform.objects.all()
    serializer_class = PlataformSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class GenreViewSet(viewsets.ModelViewSet):
    """Tabela de criação dos gêneros"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GamePlataformViewSet(viewsets.ModelViewSet):
    """Tabela de relação entre plataformas e os jogos"""
    queryset = GamePlataform.objects.all()
    serializer_class = GamePlataformSerializer

class GameGenreViewSet(viewsets.ModelViewSet):
    """Tabela de relação entre gênero e os jogos"""
    serializer_class = GameGenreSerializer
    def get_queryset(self):
        queryset = GameGenre.objects.all()
        genre_name = self.request.query_params.get('genre')
        if genre_name is not None:
            if ',' in genre_name:
                genre_name = genre_name.split(',')
                query = Q()
                for name in genre_name:
                    query = query | Q(genre__name__iexact=name)
                queryset = queryset.filter(query)
            else:
                queryset = queryset.filter(genre__name__iexact=genre_name)
        return queryset
        
class ListPlataformGame(generics.ListAPIView):
    """Listando os jogos de uma certa plataforma"""
    def get_queryset(self):
        queryset = GamePlataform.objects.filter(plataform_id=self.kwargs['pk'])
        return queryset
    serializer_class = GamePlataformSerializer

class ListGenreGame(generics.ListAPIView):
    """Listando os jogos de uma certo gênero"""
    def get_queryset(self):
        queryset = GameGenre.objects.filter(genre_id=self.kwargs['pk'])
        return queryset
    serializer_class = GameGenreSerializer
    