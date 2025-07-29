from rest_framework import serializers
from . import models

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'