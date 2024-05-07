from rest_framework import serializers

from .models import Song, Playlist, PlaylistSong

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'artist', 'release_year']

class PlaylistSongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='song.id')
    name = serializers.CharField(source='song.name')
    artist = serializers.CharField(source='song.artist')
    release_year = serializers.IntegerField(source='song.release_year')
    position = serializers.IntegerField()

class Meta:
    model = PlaylistSong
    fields = ['id', 'name', 'artist', 'release_year', 'position']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name']
