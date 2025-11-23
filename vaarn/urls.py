from django.urls import path

from . import views

app_name = "vaarn"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "character-generator",
        views.vaarn_character_creation_view,
        name="character_generator",
    ),
]
