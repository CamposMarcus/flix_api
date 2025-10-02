from django.db import models
from movies.models import Movie  # Importa o model Movie para permitir ser vinculado em uma chave estrangeira
from django.core.validators import MinValueValidator, MaxValueValidator  # Importa validadores para o projeto a serem utilizados no campo de avaliação, limitando as interações do usuário


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')  # Permite ter o nome dos filmes como selecionável na tela de avaliação
    stars = models.IntegerField(        # Adiciona um campo de números inteiros que receberá a avaliação entre os números 0 e 5.
        validators=[                   # validators são utilizados para validar a informação inserida pelo usuário, para que não seja aceito nenhum conteúdo indesejado, além do que foi validade
            MinValueValidator(0, 'Avaliação inferior à 0 estrelas não autorizada.'),  # valida que o menor valor aceito é 0 e retorna uma mensagem de erro caso um valor menor seja inserido
            MaxValueValidator(5, 'Avaliação superior à 5 estrelas não autorizada.')   # valida que o maior valor aceito é 5 e retorna uma mensagem de erro caso um valor maior seja inserido
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)
