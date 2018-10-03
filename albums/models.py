from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=140,null=False)
    artist_name = models.CharField(max_length=140,null=False)
    published_year = models.IntegerField()
    genre = models.ForeignKey('Genre', related_name='genre', on_delete=models.CASCADE)

    def __str__(self):
        return self.artist_name + ' - ' + self.name + '('+str(self.published_year)+')'

class Song(models.Model):
    name = models.CharField(max_length=140,null=False)
    duration = models.DurationField()
    album = models.ForeignKey('Album', related_name='album',on_delete=models.CASCADE)

    def __str__(self):
        return self.album.name + ' - ' + self.name

class Genre(models.Model):
    name = models.CharField(max_length=140,null=False)

    def __str__(self):
        return self.name