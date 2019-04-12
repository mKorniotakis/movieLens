from django.conf.urls import url, include
from .views import *

urlpatterns = [

    url(r'^movieList/', MoviesViewSet.as_view({'get': 'list'})),
    url(r'^ratings/', RatingsViewset.as_view({'get': 'list'})),
    url(r'^tags/', TagsViewset.as_view({'get': 'list'})),

]