from django.urls import path
from .views import *


urlpatterns = [
    path('', MovieView.as_view()),
    path('/actors', ActorView.as_view()),
    path('/actorsmovies', ActorMovieView.as_view())
]