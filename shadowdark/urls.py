from django.urls import path

from . import views

app_name = "shadowdark"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("hexcrawling", views.HexCrawlingView.as_view(), name="hexcrawling"),
    path("npc_names", views.npc_name, name="npc_name"),
    path("cast-a-spell", views.cast_wizard_spell_view, name="cast_a_spell"),
    path("encounter", views.encounter_view, name="encounter"),
    path("roll-random-table", views.roll_random_table_view, name="roll_random_tables"),
    path("carousing", views.carousing_view, name="carousing"),
    path(
        "encounters-by-zone/<str:region>",
        views.select_zone_type_view,
        name="encounters_by_zone",
    ),
    path(
        "core-book-encounters", views.core_book_encounters, name="core_encounter_tables"
    ),
    path("roll-treasure", views.roll_treasure_view, name="roll_treasure"),
]
