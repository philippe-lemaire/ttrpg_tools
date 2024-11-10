from django.urls import path

from . import views

app_name = "liminal_horror"

urlpatterns = [
    path("", views.LiminalHorrorIndexView.as_view(), name="index"),
    path(
        "bloom-character-generator",
        views.bloom_character_creation_view,
        name="bloom_character_generator",
    ),
    path("bloom-fallout", views.bloom_fallout_view, name="bloom_fallout"),
]
