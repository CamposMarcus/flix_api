from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):      # Define como o nome do elemento será apresentado para o usuário. Ex: Object01 >>> Comédia
        return self.name
