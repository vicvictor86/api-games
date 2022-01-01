from rest_framework import viewsets, generics, filters
from games.models import *
from games.serializer import *
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    """Lista de jogos disponíveis, capaz de filtrar pelo id, nome e faixa de preço"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'name']
    def get_queryset(self):
        queryset = Game.objects.all()
        game_price = self.request.query_params.get('price')
        if game_price is not None:
            if ',' in game_price:
                game_price = game_price.split(',')
                if len(game_price) > 2:
                    #Ver algum erro pois não deve ter mais que 2 elementos para faixa de preço
                    return queryset
                query = Q(price__gte=game_price[0]) & Q(price__lte=game_price[1])
                queryset = queryset.filter(query)
            else:
                queryset = queryset.filter(price=game_price)
        return queryset

class PlataformViewSet(viewsets.ModelViewSet):
    queryset = Plataform.objects.all()
    serializer_class = PlataformSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']

class GenreViewSet(viewsets.ModelViewSet):
    """Tabela de criação dos gêneros"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']

class GamePlataformViewSet(viewsets.ModelViewSet):
    """Tabela de relação entre plataformas e os jogos"""
    queryset = GamePlataform.objects.all()
    serializer_class = GamePlataformSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']

class GameGenreViewSet(viewsets.ModelViewSet):
    """Tabela de relação entre gênero e os jogos"""
    serializer_class = GameGenreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']
    def get_queryset(self):
        queryset = GameGenre.objects.all()
        genre_name = self.request.query_params.get('genre')
        if genre_name is not None:
            genre_name = genre_name.lower()
            if ',' in genre_name:
                genre_name = genre_name.split(',')
                queryset = queryset.filter(genre__name__in=genre_name)
            else:
                queryset = queryset.filter(genre__name__icontains=genre_name)
        return queryset
        
class ListPlataformGame(generics.ListAPIView):
    """Listando os jogos de uma certa plataforma"""
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']
    def get_queryset(self):
        queryset = GamePlataform.objects.filter(plataform_id=self.kwargs['pk'])
        return queryset
    serializer_class = GamePlataformSerializer

class ListGenreGame(generics.ListAPIView):
    """Listando os jogos de uma certo gênero"""
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id']
    def get_queryset(self):
        queryset = GameGenre.objects.filter(genre_id=self.kwargs['pk'])
        return queryset
    serializer_class = GameGenreSerializer

class ListFullGames(viewsets.ModelViewSet):
    """Mostrará todas as informações disponíveis para os jogos"""
    queryset = Game.objects.prefetch_related('plataforms')
    queryset = Game.objects.prefetch_related('genres')
    serializer_class = GameFullInformationsSerializer
