from django.db import models

NATIONALITY_CHOICES = (          # Cria uma variável fora da classe para armazenas opções de paises. Estas opções serão utilizadas na
    ('USA', 'Estados Unidos'),   # variável de nacionalidade, impedindo que o usuário escreva qualquer coisa diferente daquilo que
    ('BRAZIL', 'Brasil'),        # está pré definido no código
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
