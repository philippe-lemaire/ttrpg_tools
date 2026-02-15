from django.urls import path

from . import views

app_name = "cairn"

urlpatterns = [
    path("", views.CairnIndexView.as_view(), name="index"),
    path("random", views.generate_character, name="generate_character"),
    path("choice", views.generate_with_background, name="generate_with_background"),
    path("dungeon-events", views.dungeon_events_view, name="dungeon_events"),
    path("wilderness-events", views.wilderness_events_view, name="wilderness_events"),
    path("reaction-roll", views.reaction_roll_view, name="reaction_roll"),
    path("npc", views.generate_cairn_npc_view, name="generate_npc"),
]
