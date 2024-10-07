from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
