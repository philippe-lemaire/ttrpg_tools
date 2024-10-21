from django.urls import path

from . import views

app_name = "into_the_odd"

urlpatterns = [
    path("", views.IntoTheOddIndexView.as_view(), name="index"),
    path("character", views.create_character, name="create_character"),
    path(
        "mutant_character",
        views.create_mutant_character,
        name="create_mutant_character",
    ),
    path(
        "unhuman_character",
        views.create_unhuman_character,
        name="create_unhuman_character",
    ),
    path(
        "simple_folk_character",
        views.create_simple_folk_character,
        name="create_simple_folk_character",
    ),
    path("lackeys", views.create_lackeys, name="create_lackeys"),
    path("NPC", views.create_npc, name="create_npc"),
    path("island", views.create_island, name="create_island"),
    path("street", views.create_street, name="create_street"),
    path("route", views.create_route, name="create_route"),
    path("business", views.create_business, name="create_business"),
    path("council", views.council_decision, name="council_decision"),
    path("astralcult", views.create_astral_cult, name="astral_cult"),
    path("weird_creature", views.create_creature, name="create_creature"),
    path("beyond_the_darkness", views.create_beyond, name="create_beyond"),
    path("I_eat_the_stuff", views.i_eat_the_stuff, name="i_eat_the_stuff"),
    path(
        "is_this_thing_an_arcanum",
        views.is_this_thing_an_arcanum,
        name="is_this_thing_an_arcanum",
    ),
]
