from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album

from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        found_album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        return Song.objects.filter(album_id=found_album.id)

    def perform_create(self, serializer):
        found_album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        return serializer.save(album_id=found_album.id)
