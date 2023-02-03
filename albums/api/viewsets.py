from rest_framework import viewsets
from albums.api import serializers
from albums.models import Albums


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlbumSerializer
    queryset = Albums.objects.all()
