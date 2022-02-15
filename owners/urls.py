from django.urls import path
from .views      import OwnerView, DogView

# http://localhost:8000/owners  Get

urlpatterns = [
    path('/owners', OwnerView.as_view()),
    path('/dogs', DogView.as_view())
]