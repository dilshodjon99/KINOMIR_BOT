from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/create/', MoviesCreateView.as_view()),
    path('movies/<id>/', MoviesDetailView),
    path('films/', FilmsListView),
]
