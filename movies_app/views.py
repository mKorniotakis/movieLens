from django.shortcuts import render
from rest_framework import viewsets
from movies_app.serializers import *


class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class RatingsViewset(viewsets.ModelViewSet):

    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class TagsViewset(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer