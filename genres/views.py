from genres.models import Genre  # Importa o model Genre para a tela de views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Biblioteca do RF que permite limitar acesso à views apenas aos usuários que possuam token de acesso
from genres.serializers import GenreModelSerializer
from app.permissions import GlobalDefaultPermission
# import json # Biblioteca nativa do Python para ler e interpretar json
# # from django.http import JsonResponse  # Importa o pacote que permite tabalhar com formato Json
# from django.views.decorators.csrf import csrf_exempt # Importa um pacote de proteção nativo do django. Sem ele o métido POST dará erro
# from django.shortcuts import get_object_or_404 # Tenta dar um GET no objeto. Se ele não existir, retorna erro 404


class GenreCreateListView(generics.ListCreateAPIView):  # Implementa a class based view do Rest Framework para listar e criar registros. Herda de generics do Framework
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)  # Linha de código que limita o acesso à view apenas para quem estiver autenticado
    queryset = Genre.objects.all()    # Captura todos os registros no model Genre e atribui à uma variável
    serializer_class = GenreModelSerializer  # Serialziador da view. Responsável por traduzir a informação para formato dicionário


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()  # Cria uma lista contendo todos os genres cadastrados e atribui a uma variável
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]  # Dictionary comprehention para criar uma lista de dicionários
#         return JsonResponse (data, safe=False)  # safe=False Controla se apenas objetos dicionários podem ser serializados

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8')) # request.body.decode('utf-8'): Captura o corpo da request sendo enviado pelo usuário e fomata em estilo utf-8. # json.loads: Transforma uma string enviada em um objeto dicionário
#         new_genre = Genre(name=data['name'])  # Utiliza o form Genre para receber o nome do genero enviado pelo usuário e aloca em uma variável
#         new_genre.save()    # Salva os dados passados para a variável no banco de dados
#         return JsonResponse(        # Gera um retorno para o usuário em formato json onde
#             {'id': new_genre.id,    # Será retornado o Id e nome do genero criado pelo usuário
#             'name': new_genre.name
#             },
#             status=201)      # Este status=201 indica que, em protocolo HTTP, indica o status de 'created', ou seja, significa que foi criado um objeto com sucesso.

# @csrf_exempt
# def genre_detail_view(request, pk): # Necessário inserir o pk como parâmetro para permitir trabalhar com 1 item em específico
#     genre = get_object_or_404(Genre, pk=pk) # Faz uma query nos dados e retorna o item cuja chave primaria corresponde à chave solicitada pelo usuário

#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name} # Monta e salva na variável o objeto desejado pelo usuário
#         return JsonResponse(data) # Retorna para o usuário a informação em formato json

#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id': genre.id, 'name': genre.name}
#         )

#     elif request.method == 'DELETE':
#         genre.delete()  # Deleta o genero sinalizado na url do banco de dados
#         return JsonResponse(        # Retorna uma confirmação de deleção em formato json
#             {'message': 'Gênero excluído com sucesso!'
#         }, status=204,)  # Status que indica que um elemento foi deletado do registro
