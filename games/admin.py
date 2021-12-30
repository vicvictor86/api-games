from django.contrib import admin
from games.models import *

# Register your models here.
class GameGenres(admin.ModelAdmin):
    list_display = ('id', 'game', 'genre')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(GameGenre, GameGenres)