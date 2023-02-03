from rest_framework import serializers
from albums.models import Albums


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Albums
        fields = '__all__'
        
        