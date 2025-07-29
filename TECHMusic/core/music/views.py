from rest_framework import generics
from . import serializers, models

class MusicListView(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.MusicSerializer