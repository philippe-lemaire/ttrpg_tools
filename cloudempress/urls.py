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
]
