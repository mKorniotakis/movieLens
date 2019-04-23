from django.conf.urls import url, include
from django.urls import path
from .views import *
from . import views

urlpatterns = [

    url(r'^movieList/', MoviesViewSet.as_view({'get': 'list'})),
    url(r'^ratings/', RatingsViewset.as_view({'get': 'list'})),
    url(r'^tags/', TagsViewset.as_view({'get': 'list'})),
    path('index.html/', views.MovieList.as_view()),
]