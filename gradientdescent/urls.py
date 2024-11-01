from django.urls import path

from . import views

app_name = "gradientdescent"

urlpatterns = [
    path("encounters", views.roll_encounters_view, name="roll_encounters"),
    path("d100_tables/<str:table_name>", views.d100_table_view, name="d100_tables"),
    path("monarchs", views.MonarchListView.as_view(), name="monarchs"),
    path(
        "monarchs/<slug:campaign_name>",
        views.checkout_monarch,
        name="checkout_monarch",
    ),
]
