from . import views
from django.urls import path

app_name="owners"
urlpatterns = [
    path("", views.OwnersView.as_view()),
    path("pet/", views.DogsView.as_view())
]
