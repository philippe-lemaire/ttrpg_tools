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
    path("create-byway", views.create_byways, name="create_byway"),
    path("roll-settlement", views.roll_settlement, name="roll_settlement"),
    path("roll-cavern", views.roll_cavern, name="roll_cavern"),
    path("roll-mystling", views.roll_mystling, name="roll_mystling"),
]
