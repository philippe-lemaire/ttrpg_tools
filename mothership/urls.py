from django.urls import path
from . import views

app_name = "mothership"

urlpatterns = [
    path("", views.MothershipIndexView.as_view(), name="index"),
    path("create-character", views.create_character, name="create_character"),
    path(
        "create-character-step-2",
        views.create_character_step_2,
        name="create_character_step_2",
    ),
    path("search-tables", views.search_tables, name="search_tables"),
    path("wages-of-sin/bounties", views.BountyListView.as_view(), name="bounties"),
    path(
        "wages-of-sin/bounties/<int:pk>",
        views.BountyDetailView.as_view(),
        name="bounty_detail",
    ),
]
