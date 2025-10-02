from rest_framework import serializers  # Importa o pacote de serializadores do rest framework
from genres.models import Genre  # Importa o model Genre da aplicação genres


class GenreModelSerializer(serializers.ModelSerializer):  # Cria uma class based view que recebe de serializers o ModelSerializers

    class Meta:
        model = Genre  # Define o model a ser trabalhado
        fields = '__all__'  # Define quais campos serão considerados nesta etapa.
