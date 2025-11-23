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
    path("hypergeometry/random-codex", views.vaarn_gen_codex_view, name="roll_codex"),
    path(
        "hypergeometry/random-mishap",
        views.vaarn_hypergeometry_mishap_view,
        name="roll_mishap",
    ),
    path("mutations", views.vaarn_get_mutation_view, name="roll_mutation"),
]
