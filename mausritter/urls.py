from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "mausritter"

urlpatterns = [
    path("", views.index, name="index"),
    path("colonie_de_souris/", views.generate_colony, name="generate_colony"),
    path(
        "site_d_aventure/",
        views.generate_adventure_site,
        name="generate_adventure_site",
    ),
    path("souris_non_joueuse/", views.generate_npc_mouse, name="generate_npc_mouse"),
    path("graine_d_aventure/", views.generate_seed, name="generate_seed"),
    path("trouver_un_sort/", views.generate_spell, name="generate_spell"),
    path(
        "trouver_une_épée_magique/",
        views.generate_magic_sword,
        name="generate_magic_sword",
    ),
    path(
        "créer_une_souris_joueuse/",
        views.generate_mouse_pc,
        name="generate_mouse_pc",
    ),
    path("trouver_des_tresors/", views.roll_treasure, name="roll_treasure"),
    path(
        "feuilles_de_personnage_en_ligne/",
        TemplateView.as_view(template_name="mausritter/character_keeper.html"),
        name="character_keeper",
    ),
    path("lancer_un_sort/", views.roll_spell, name="roll_spell"),
    path("creatures/", views.CreatureListView.as_view(), name="creature_index"),
    path(
        "creatures/<int:pk>",
        views.CreatureDetailView.as_view(),
        name="creature_detail",
    ),
]
