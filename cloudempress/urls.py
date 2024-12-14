from django.urls import path
from . import views

app_name = "cloudempress"

urlpatterns = [
    path("", views.CloudEmpressIndexView.as_view(), name="index"),
    path("create-character", views.create_character, name="create_character"),
    path(
        "create-character-step-2",
        views.create_character_step_2,
        name="create_character_step_2",
    ),
    path("create-byway", views.create_byway, name="create_byway"),
    path("roll-settlement", views.roll_settlement, name="roll_settlement"),
    path("roll-cavern", views.roll_cavern, name="roll_cavern"),
    path("roll-mystling", views.roll_mystling, name="roll_mystling"),
    path("roll-guild", views.roll_guild, name="roll_guild"),
    path("roll-exit", views.get_exit, name="roll_exit"),
    path("roll-forgotten-mine", views.roll_forgotten_mine, name="roll_forgotten_mine"),
    path(
        "roll-encounter-unseen-city",
        views.roll_encounter_unseen_city,
        name="roll_encounter",
    ),
    path("unseen-city-spells", views.spells_view, name="spells"),
    path(
        "roll-encounter-land-of-cicadas",
        views.roll_encounter_land_of_cicadas,
        name="roll_encounter_land_of_cicadas",
    ),
    path(
        "roll-hunt-and-gather-land-of-cicadas",
        views.roll_hunt_and_gather_land_of_cicadas,
        name="roll_hunt_and_gather_land_of_cicadas",
    ),
]
