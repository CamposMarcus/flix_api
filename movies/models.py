from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')  # Cria uma chave estrangeira que busca opções do app criado em genres
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movie')  # Cria uma ligação muitos para muitos pois um filme possui vários atores e um ator pode estar em vários filmes
    resume = models.TextField(null=True, blank=True)  # Cria um campo de texto livre

    def __str__(self):
        return self.title
