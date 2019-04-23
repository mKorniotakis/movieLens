from django.shortcuts import render
from rest_framework import viewsets
from movies_app.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MovieList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Movies.objects.all()
        return Response({'movies': queryset})


class RatingsViewset(viewsets.ModelViewSet):

    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class TagsViewset(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer