from django.urls import path
from . import views  # O arquivo views e o arquivo urls estão no mesmo nivel e portanto não é necessário realizar ma importação de maneira semelhante ao que é feito para os demais


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genres-create-list'),  # Necessário colocar o views. na frente do nome da view que deseja chamar
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
