from django.urls import path
from .views import *

urlpatterns = [
    path('', BookApi.as_view()),
    path('author', AuthorApi.as_view()),
    path('genre', GenreApi.as_view()),
    path('<int:pk>/', DetailBookApi.as_view()),
    path('author/<int:pk>/', DetailAuthorApi.as_view()),
    path('genre/<int:pk>/', DetailGenreApi.as_view()),
]