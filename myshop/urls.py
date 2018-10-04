"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from albums.serializers import AlbumViewSet, SongViewSet, GenreViewSet as MusicGenreViewSet, ArtistViewSet
from books.serializers import BookViewSet, AuthorViewSet, GenreViewSet as BookGenreViewSet
from albums import views as albumViews
from books import views as bookViews

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'music-genres', MusicGenreViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'book-genres', BookGenreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Albums Rest Views
    url(r'^albums/$', albumViews.AlbumList.as_view()),
    url(r'^albums/(?P<pk>[0-9]+)/$', albumViews.AlbumDetail.as_view()),
    url(r'^artists/$', albumViews.ArtistList.as_view()),
    url(r'^artists/(?P<pk>[0-9]+)/$', albumViews.ArtistDetail.as_view()),
    url(r'^songs/$', albumViews.SongList.as_view()),
    url(r'^songs/(?P<pk>[0-9]+)/$', albumViews.SongDetail.as_view()),
    url(r'^music-genres/$', albumViews.GenreList.as_view()),
    url(r'^music-genres/(?P<pk>[0-9]+)/$', albumViews.GenreDetail.as_view()),

    # Books Rest Views
    url(r'^books/$', bookViews.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', bookViews.BookDetail.as_view()),
    url(r'^authors/$', bookViews.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', bookViews.AuthorDetail.as_view()),
    url(r'^book-genres/$', bookViews.GenreList.as_view()),
    url(r'^book-genres/(?P<pk>[0-9]+)/$', bookViews.GenreDetail.as_view()),
]