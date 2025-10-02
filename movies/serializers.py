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
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = round(obj.reviews.aggregate(Avg('stars'))['stars__avg'], 1)

        if rate:
            return rate

        return None
