from django.urls import path
from . import views

app_name = "tor"

urlpatterns = [
    path("", views.TorIndexView.as_view(), name="index"),
    path("action-resolution", views.action_resolution_view, name="action_resolution"),
    path("treasure", views.treasure_hoard_view, name="treasure"),
    path(
        "strider-mode/telling-table",
        views.strider_telling_table_view,
        name="strider_telling_table",
    ),
    path(
        "strider-mode/fortune-tables",
        views.fortune_tables_view,
        name="strider_fortune_table",
    ),
    path("nameless-things", views.nameless_thing_view, name="nameless_thing"),
    path(
        "strider-mode/solo-journey",
        views.strider_solo_journey_view,
        name="strider_solo_journey",
    ),
    path(
        "strider-mode/revelation-episode",
        views.strider_revelation_episode_view,
        name="strider_revelation_episode",
    ),
]
