from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()  # Define de qual tabela o Django deve buscar os dados

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):  # Modelo mais basico das APIviews. Permite que views personalizadas sejam cradas do 0, sem que existam pré-definições.
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):  # Escreve o métido GET a ser enviado pelo usuário.
        total_movies = self.queryset.count()  # Conta a quantidade de filmes cadastrados. self. aponta para a classe pai e permite acessar a variável criada nela
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  # .values('genre__name') retorna uma coluna com os nomes dos generos de cada filme. '.annotate(count= Count('id')' faz um groupby na coluna criada acima e aplica uma contagem de valores
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }, status=status.HTTP_200_OK)
