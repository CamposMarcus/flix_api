from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.serializers import ActorModelSerializer
from actors.models import Actor
from app.permissions import GlobalDefaultPermission


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class ActorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
