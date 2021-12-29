from rest_framework import viewsets
from games.models import *
from games.serializer import *

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlataformViewSet(viewsets.ModelViewSet):
    queryset = Plataform.objects.all()
    serializer_class = PlataformSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GamePlataformViewSet(viewsets.ModelViewSet):
    queryset = GamePlataform.objects.all()
    serializer_class = GamePlataformSerializer

class GameGenreViewSet(viewsets.ModelViewSet):
    queryset = GameGenre.objects.all()
    serializer_class = GameGenreSerializer