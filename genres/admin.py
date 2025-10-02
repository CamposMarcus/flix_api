from django.contrib import admin
from genres.models import Genre  # Importa a classe Genre para o arquivo admin.py


@admin.register(Genre)  # Registra a classe model Genre na tela de Admin
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # list_display representa as colunas a serem apresentadas na tabela
