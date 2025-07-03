from django.urls import path

from . import views

app_name = "ose"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "monsters/by_hit_dice/<int:hit_dice>",
        views.filtered_monster_list,
        name="monster_by_hit_dice",
    ),
    path("monsters/", views.MonsterListView.as_view(), name="monster_list"),
    path(
        "monsters/<int:pk>",
        views.MonsterDetailView.as_view(),
        name="monster_detail",
    ),
    path("adventuring_party", views.adventuring_party_view, name="adventuring_party"),
    path("hoards", views.Hoard_index.as_view(), name="hoards"),
    path("hoard/<str:type_>", views.hoard_result, name="hoard_result"),
    path(
        "magic_items/alchemist_beaker", views.alchemist_beaker, name="alchemist_beaker"
    ),
    path(
        "magic_items/deck_of_many_things",
        views.deck_of_many_things,
        name="deck_of_many_things",
    ),
    path(
        "magic_items/figurines_of_wondrous_power", views.figurine_view, name="figurine"
    ),
    path("encounters/heretic_gnomes", views.heretic_gnomes_view, name="heretic_gnomes"),
]
