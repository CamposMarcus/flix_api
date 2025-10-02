from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorModelSerializer
from genres.serializers import GenreModelSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta():
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):  # Cria uma função de validação. Precisa começar com 'validade_' e ter o nome do campo a ser validado.
        if value.year < 1920:   # Representa a regra a ser cumprida
            raise serializers.ValidationError('Filmes anteiores à 1920 não permitidos')  # Sobe um erro de validação com uma mensagem caso a validação falhe
        return value    # Se for validado, retorna o valor

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve conter mais do que 500 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorModelSerializer(many=True)
    genre = GenreModelSerializer()
    rate = serializers.SerializerMethodField(read_only=True)  # Adiciona um campo extra ao Model original. Este campo será um campo calculado.
# 'read_only=True' define que ele apenas irá aparecer no método GET

    class Meta():
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = round(obj.reviews.aggregate(Avg('stars'))['stars__avg'], 1)
# obj.reviews.aggregate(Avg('stars')) retorna a lista de filmes com todos os campos e agrega um novo campo. Nesse caso, o novo campo é uma média de estrelas
# ['star__avg'] garante que seja retornado apenas o valor da média de estrelas para a variável.
# Necessário importar o modo Avg do models do Django

        if rate:    # Se houver rate, retorna o rate. Se não houver rate, retorna None
            return rate

        return None

# MODO ANTIGO E SEM UTILIZAR RM DO DJANGO
    # def get_rate(self, obj): # Para um campo calculado é OBRIGATÓRIO o nome da função começar com 'get_' e ter o nome da variável na sequência 'rate'
    # reviews = obj.reviews.all() # Coleta todas as reviews do filme, que é o objeto sendo avaliado, e salva em uma varíavel

    #     if reviews: # Cria uma condição para verificar se existem reviews cadastrados para o filme
    #         sum_reviews = 0 # Define uma variável para receber a soma dos reviews e define como valor inicial o 0

    #         for review in reviews:  # Define um loop para percorrer todos os reviews dentro dos reviews de cada filme
    #             sum_reviews += review.stars # Para cada review destinada a um filme, soma o valor da review na variável criada

    #         review_count = reviews.count() # Conta a quantidade de reviews registradas para um filme

    #         return round(sum_reviews / review_count, 1) # Dívide a soma de estrelas pela quantidade de avaliações e arredonda para 1 casa decimal

    #     return None # Se não houver nenhuma review para o filme retorna o valor nulo (null)
