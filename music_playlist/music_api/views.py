from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import F

from .models import Song, Playlist, PlaylistSong
from .serializers import SongSerializer, PlaylistSerializer, PlaylistSongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

def get_queryset(self):
    queryset = Song.objects.all()
    query = self.request.query_params.get('q')
    if query:
        queryset = queryset.filter(name__icontains=query)
    return queryset

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

def get_queryset(self):
    queryset = Playlist.objects.all()
    query = self.request.query_params.get('q')
    if query:
        queryset = queryset.filter(name__icontains=query)
    return queryset

@action(detail=True, methods=['get'])
def songs(self, request, pk=None):
    playlist = self.get_object()
    songs = playlist.playlistsong_set.all()
    paginator = self.paginate_queryset(songs)
    serializer = PlaylistSongSerializer(paginator.object_list, many=True)
    return self.get_paginated_response(serializer.data)

@action(detail=True, methods=['put'])
def move_song(self, request, pk=None):
    playlist = self.get_object()
    song_id = request.data.get('song_id')
    new_position = request.data.get('position')

    try:
        playlist_song = playlist.playlistsong_set.get(song_id=song_id)
    except PlaylistSong.DoesNotExist:
        return Response({'error': 'Song not found in playlist'}, status=status.HTTP_404_NOT_FOUND)

    old_position = playlist_song.position

    if new_position > old_position:
        playlist.playlistsong_set.filter(position__gt=old_position, position__lte=new_position).update(
            position=F('position') - 1)
    else:
        playlist.playlistsong_set.filter(position__lt=old_position, position__gte=new_position).update(
            position=F('position') + 1)

    playlist_song.position = new_position
    playlist_song.save()

    return Response({'position': new_position}, status=status.HTTP_200_OK)

@action(detail=True, methods=['delete'])
def remove_song(self, request, pk=None):
    playlist = self.get_object()
    song_id = request.data.get('song_id')

    try:
        playlist_song = playlist.playlistsong_set.get(song_id=song_id)
    except PlaylistSong.DoesNotExist:
        return Response({'error': 'Song not found in playlist'}, status=status.HTTP_404_NOT_FOUND)

    position = playlist_song.position
    playlist_song.delete()

    playlist.playlistsong_set.filter(position__gt=position).update(position=F('position') - 1)

    return Response(status=status.HTTP_200_OK)

def create(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    playlist = serializer.save()

    song_ids = request.data.get('songs', [])
    position = 1
    for song_id in song_ids:
        try:
            song = Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            continue

        PlaylistSong.objects.create(playlist=playlist, song=song, position=position)
        position += 1

    return Response(serializer.data, status=status.HTTP_201_CREATED)