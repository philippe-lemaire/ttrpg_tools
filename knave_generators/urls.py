from django.urls import path

from . import views

app_name = "knave_generators"

urlpatterns = [
    path("", views.KnaveIndex.as_view(), name="knave_index"),
    path("player-character", views.create_player_character, name="player-character"),
    path(
        "create-custom-character",
        views.create_custom_player_character,
        name="custom-player-character",
    ),
    path(
        "player-character/level-up",
        views.level_up_character,
        name="level-up",
    ),
    path("weather-forecast", views.roll_weather_view, name="weather-forecast"),
    path("travel-rules", views.TravelRulesView.as_view(), name="travel-rules"),
    path("delve-rules", views.DelveRulesView.as_view(), name="delve-rules"),
    path("alchemy-rules", views.AlchemyRulesView.as_view(), name="alchemy-rules"),
    path(
        "relic-magic-rules",
        views.RelicMagicRulesView.as_view(),
        name="relic-magic-rules",
    ),
    path("spells", views.SpellListView.as_view(), name="spell-list"),
    path("tables", views.list_tables, name="list-tables"),
    path("tables/<str:table_name>", views.get_table, name="get-table"),
    path("inn", views.roll_tavern_name, name="inn"),
    path("npc", views.roll_npc, name="npc"),
    path("encounters", views.EncountersRulesView.as_view(), name="encounters"),
    path("random-monster", views.roll_random_monster, name="random-monster"),
    path("random-spell", views.roll_random_spell, name="random-spell"),
    path("monsters", views.MonsterListView.as_view(), name="monster_list"),
    path(
        "monsters/<int:pk>",
        views.MonsterDetailView.as_view(),
        name="monster_detail",
    ),
]
