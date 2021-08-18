from . import views
from django.urls import path




app_name="movies"
urlpatterns = [
    path("", views.ActorsView.as_view()),
    path("moviesandactors/", views.MoviesView.as_view())
]
