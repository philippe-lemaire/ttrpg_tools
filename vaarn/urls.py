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
    path(
        "character-generator-chosing-ancestry",
        views.vaarn_character_creation_chosing_ancestry,
        name="character_generator_with_ancestry",
    ),
    path("hypergeometry/random-codex", views.vaarn_gen_codex_view, name="roll_codex"),
    path(
        "hypergeometry/random-mishap",
        views.vaarn_hypergeometry_mishap_view,
        name="roll_mishap",
    ),
    path("mutations", views.vaarn_get_mutation_view, name="roll_mutation"),
    path(
        "wounds/biological-wounds",
        views.vaarn_biological_wounds_view,
        name="biological_wounds",
    ),
    path(
        "wounds/synthetic-wounds",
        views.vaarn_synthetic_wounds_view,
        name="synthetic_wounds",
    ),
    path(
        "generate-follower",
        views.vaarn_generate_follower_view,
        name="generate_follower",
    ),
    path(
        "generate-mercenary",
        views.vaarn_generate_mercenary_view,
        name="generate_mercenary",
    ),
    path(
        "cybernetic-implants",
        views.vaarn_cybernetic_implants,
        name="cybernetic_implants",
    ),
    path(
        "exotica",
        views.vaarn_exotica,
        name="exotica",
    ),
    path("bloomboons", views.vaarn_bloomboons, name="bloomboons"),
    path("random-settlement", views.vaarn_roll_settlement_view, name="roll_settlement"),
]
