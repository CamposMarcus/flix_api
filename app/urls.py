from django.contrib import admin
from django.urls import path, include  # include busca dentro de um app pelo arquivo urls e captura todas as urls declaradas


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('authentication.urls')),
]
