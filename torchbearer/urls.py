from django.urls import path

from . import views

app_name = "torchbearer"

urlpatterns = [
    path("", views.TorchbearerIndexView.as_view(), name="index"),
    path("loot-rules", views.TorchbearerLootRules.as_view(), name="loot_rules"),
    path("loot-tables", views.loot_tables_view, name="loot_tables"),
    path("loot-subtables", views.loot_subtables_view, name="loot_subtables"),
    path(
        "camp-event-rules",
        views.TorchbearerCampEventRules.as_view(),
        name="camp_event_rules",
    ),
    path("camp-events", views.camp_events_view, name="camp_events"),
]
