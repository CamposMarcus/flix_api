import csv
from datetime import datetime
from django.core.management.base import BaseCommand  # Biblioteca que permite trabalhar com comandos personalizados
from actors.models import Actor


class Command(BaseCommand):  # Classe padrão para se criar um comando

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores',
        )

    def handle(self, *args, **options):  # Função padrão para lidar com o comando. Abaixo dela fica todo o código que se deseja executar
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:  # Abre o arquivo csv com os dados que se deseja automatizar
            reader = csv.DictReader(file)  # Identifica os cabeçalhos das colunas
            for row in reader:
                name = row['name']  # Retorna o nome à cada linha
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()  # Retorna a idade à cada linha e converte a string para o formato de data
                nationality = row['nationality']  # Retorna a nacionalidade à cada linha

                self.stdout.write(self.style.NOTICE(name))  # PErmite verificar andamento do processo

                Actor.objects.create(  # Acessa o model de atores na função de criação e recebe os campos a serem preenchidos no formulário.
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))  # Recurso do 'command' que possui a mesma função do 'print', porém com um visual mais moderno. Retorna um texto verde.
# stdout representa a saída do comando
