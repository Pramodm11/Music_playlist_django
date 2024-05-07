from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    release_year = models.IntegerField()

def __str__(self):
    return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, through='PlaylistSong')

def __str__(self):
    return self.name

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

class Meta:
    ordering = ['position']
    unique_together = ['playlist', 'song']
