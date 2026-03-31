town_types = (
    "Bustling Metropolis",
    "Busy Crossroad",
    "Dwarven Hall",
    "Elfhome",
    "Religious Bastion",
    "Remote Village",
    "Wizard’s Tower",
)

bustling_metropolis_events = {}
busy_crossroad_events = {}
dwarven_hall_events = {}
elfhome_events = {}
religious_bastion_events = {}
remote_village_events = {}
wizard_tower_events = {}

events_dicts = (
    bustling_metropolis_events,
    busy_crossroad_events,
    dwarven_hall_events,
    elfhome_events,
    religious_bastion_events,
    remote_village_events,
    wizard_tower_events,
)
town_events_table = {k: v for k, v in zip(town_types, events_dicts)}
