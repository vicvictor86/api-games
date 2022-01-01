from django.db import models
import uuid

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Studio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    fundation = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    founders = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Plataform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    initial_release_date = models.DateField()
    description = models.CharField(max_length=1000)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    sales = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='games' ,blank=True)
    def __str__(self):
        return self.name

class GamePlataform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='plataforms')
    plataform = models.ForeignKey(Plataform, on_delete=models.CASCADE)
    def __str__(self):
        return self.plataform.name

class GameGenre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='genres')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre.name
