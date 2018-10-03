from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=140,null=False)
    last_name = models.CharField(max_length=140,null=False)
    date_of_birth = models.DateTimeField(null=True)
    biography = models.TextField()

    def __str__(self):
        return self.first_name +' '+ self.last_name

class Book(models.Model):
    title = models.CharField(max_length=140,null=False)
    description = models.TextField()
    author = models.ForeignKey('Author', related_name='author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', related_name='genre', on_delete=models.CASCADE)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=140,null=False)

    def __str__(self):
        return self.name