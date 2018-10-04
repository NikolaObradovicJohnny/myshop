from rest_framework import serializers, viewsets
from .models import Album, Artist, Song, Genre

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('id','name', 'duration','album')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id','name', 'artist', 'published_year','genre','songs')

# Serializers define the API representation.
class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id','name', 'biography','albums')

# ViewSets define the view behavior.
class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer