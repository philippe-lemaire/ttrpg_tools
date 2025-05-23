from dataclasses import dataclass
from .game_data import LIMINAL_HORROR_MODULES


@dataclass
class Archetype:
    name: str
    description: str
    take: list


archetype_data_the_bloom = (
    (
        "True Crime",
        "Everyone with a microphone has a podcast these days, and your metrics have taken a dive. The mystery surrounding Coldwater has been floating around the back channels, but you’re just the person to get to the truth of the matter.",
        "Mini shotgun mic, smartphone tripod, LED light.",
    ),
    (
        "Prodigal Child",
        "As a child, you spent your summers here in your family’s cabin by the lake. It’s been ten years since your last visit. This isn’t the town you remember.",
        "Outdated guidebook, rusted set of keys, old fishing rod.",
    ),
    (
        "Gone Squatchin’",
        "An expert in your field, you’ve been chasing the elusive Sasquatch for years, looking for proof that’ll finally convince the public. All of the evidence points here.",
        "Thermal camera, bear mace (d4 blast, nonlethal), ghillie suit.",
    ),
    (
        "Late to the Party",
        "You did the research, set the date, and booked the campground reservation, but an unexpected work task prevented you from leaving with your friends. Now they’re missing.",
        "Sleeping bag, camping backpack (+2 inventory), small survival kit.",
    ),
    (
        "Writers Retreat",
        "It’s been far too long since you put anything on your editor’s desk. Maybe some fresh air and time away from the bustling city will get the creative juices flowing.",
        "E-paper tablet, whittlin’ jackknife (d6), bottle of liquor.",
    ),
    (
        "Blue Devils",
        "The whole “solo career” hasn’t really been working out as planned. This next gig at the “Blueberry Festival” is just one of a long line of crummy shows with meager pay.",
        "Instrument of choice, vintage dynamic microphone, portable amp.",
    ),
    (
        "Passing Through",
        "Coldwater was as far as that truck driver would take you on your way to the city, but this place has a pleasant charm, so maybe you’ll stay a while.",
        "Backpack (+2 inventory), rain coat, walking stick (d6), pocket knife (d6).",
    ),
    (
        "According to Plan",
        "The reputation that precedes you is well deserved. The townsfolk are shelling out good money to ensure their silly little festival goes off without issue, and you’ve planned out everything perfectly.",
        "Laptop, multi-tool, DLSR camera, business cards.",
    ),
    (
        "On Call",
        "Coldwater doesn’t have a veterinary office, but when a farm animal gets sick, they call you. This time, it’s the wildlife that has been acting strange, and folks are getting concerned.",
        "Scalpel (d6), forceps, bottle of disinfectant, surgical clamps.",
    ),
    (
        "Enblightened",
        "The area surrounding Coldwater has some fascinating species of fungi. And, unfortunately, some destructive ones. The farmers have been complaining about lower yields, so a blight might be cropping up.",
        "Pocket microscope, small sampling kit, tree corer (d6).",
    ),
    (
        "Small Town Beat",
        "While the local regions are your passion, working this beat hasn’t resulted in a noteworthy column in years. Hopefully the Blueberry Fest is buzzworthy enough to keep you employed for a bit longer.",
        "Voice recorder, digital camera, notebook, taser (d6, targets DEX).",
    ),
    (
        "Horror Helmer",
        "You’ve sold a script for “the next great slasher”, but the studio wants a filming location locked down before the next meeting or the film will be tabled. On paper, Coldwater is perfect considering your shoe-string budget.",
        "360 degree camera & pole, script, light meter, stack of blank rental agreements.",
    ),
    (
        "Avant-Gardener",
        "There’s some pretty wild culinary trends going on in the city, and word has it that Coldwater is an untapped goldmine for unique ingredients to forage. Maybe you’ll make a proper career out of this.",
        "Hooked knife (d6), collapsible shovel (d6), foraging basket.",
    ),
    (
        "Grom",
        "You’re green, but the local bike parks have been a breeze. You’ve got to train on the unproven trails if you’re going to get good enough to go pro.",
        "Mountain bike, anti-collision shirt (+1 armor), full face helmet (+1 armor when wearing), action camera.",
    ),
    (
        "GSR",
        "While the passion is still there, the field research for your master's thesis, <em>“Small Towns, From Prosperity to Ruin”</em>, has been frustrating. Hopefully Coldwater will be the final stop.",
        "Laptop, binder full of Coldwater research, letter of introduction.",
    ),
    (
        "Fraud Finder",
        "Your company has been buried processing the stack of insurance claims that have come out of this region over the past year. The vagueness in the reports has triggered an in-person audit.",
        "Insurance claims, pepper spray (d6, nonlethal), digital camera.",
    ),
    (
        "Rainmaker",
        "The company you work for began as a “Mom & Pop” general contractor, but a few lucky jobs have left them flush with cash and looking to expand into real estate. This dated town is ripe for new development.",
        "Company credit card, hard hat (+1 armor), reflective vest.",
    ),
    (
        "Golden Years",
        "After decades of stressful work, you’ve finally retired. A few years early at that! Away from the bustle of the city, Coldwater seems like it’s going to be a great place to settle into.",
        "House in Coldwater, collapsible hiking pole (d6), Anna Stone novel.",
    ),
    (
        "Phase 1 ESA",
        "Government funding has surprisingly been allocated for the revitalization of public land in Coldwater. You’ve been brought in to conduct an initial assessment, identifying unregistered landfills and point sources that pose a threat to environmental receptors.",
        "Annotated map, storage clipboard, 16’ telescopic grade rod (d6). ",
    ),
    (
        "Blind Cast",
        "Rumor has it that Coldwater Lake has some of the best fishing in the area. Folks would pay good money for a charter to take them to the best spots, so it’s time to scope them out.",
        "Pedal drive kayak, collapsible rod (d6), tackle box, gill stringer.",
    ),
)

archetype_data_hungry_hollow = (
    (
        "Burned",
        "The Bureau interfered with your life, and you want to find enough evidence to bring them to justice. During an operation they may have contributed to the death or loss of a loved one, instituted a cover up that destabilized your life, or attempted to capture you. ",
        "An old photograph, leather jacket (+1 Armor), revolver (d6).",
    ),
    (
        "Final Girl",
        "Your life has already been touched by the paranatural. You survived, but others didn’t. There’s no going back to your old life now, there are too many questions left. ",
        "Fallout, bloodstained jacket, machete (d6).",
    ),
    (
        "Career Criminal",
        "You’ve done a lot of jobs, many of them successful. You like to think of yourself as a jack-of-all-trades but that’s probably not what the Feds think. ",
        "Burner phone, lockpicking kit, unregistered firearm (d6).",
    ),
    (
        "Without a Trace",
        "She’s gone. You’ve been searching, but no-one seems to know anything. However, she wasn’t the only one to disappear under mysterious circumstances. Your quest for answers has brought you to face horrors beyond imagining. ",
        "File of evidence, “borrowed” handgun (d6), deteriorated video message from that night.",
    ),
    (
        "Breadcrumbs",
        "Your quest for the truth has led you to dark places, breaking norms, and pushing past laws. Your search has brought you to the Archivist’s attention, and now they’re providing you an opportunity to peek behind the veil. ",
        "Leather jacket (+1 Armor), old photograph, service revolver (d6).",
    ),
    (
        "Relic-Touched",
        "A resonant artifact is in your possession. Not only do you have access to its power, but being its keeper puts a target on your back.  Sometimes being on the offensive is a better tactic. ",
        "Resonant Artifact (p. 104), stylish leather jacket (+1 Armor).",
    ),
    (
        "Too Old",
        "The fight against the horrors that lie in the shadows is never ending, and you’ve been doing this a long time. It’s time to find someone to pass the torch to. ",
        "Old Ring (+1 Stability), hidden cane sword (d8), detailed journal.",
    ),
    (
        "Sleeper Agent",
        "You are secretly a Bureau agent. One of the above Archetypes acts as your cover. How committed are you? How close are you to turning double agent? ",
        "Palm pistol (d6, discrete), garrote (d8, brutal), cyanide pill.",
    ),
)

archetype_data_base_game = (
    (
        "Factory Worker",
        "",
        "Industrial apron (+1 Armor), safety harness, thermos.",
    ),
    (
        "Bus Driver",
        "",
        "Lunchbox, comprehensive road map, taser (d6, non-lethal).",
    ),
    (
        "Mechanic",
        "",
        "Adjustable wrench (d6), portable toolbox, electrical tape, brake cleaner.",
    ),
    (
        "Garbage Collector",
        "",
        "Cut resistant gloves (+1 Armor), hi-vis vest, reach extender, safety glasses.",
    ),
    (
        "Emergency Medical Technician (EMT)",
        "",
        "Medkit, trauma shears, stethoscope, WAG bag.",
    ),
    (
        "Store Clerk",
        "",
        "Box cutter (d6), walkie talkies, name tag, incredibly comfortable shoes.",
    ),
    (
        "Artist",
        "",
        "Artistic tool of choice, notebook, camera, small but passionate fan base.",
    ),
    (
        "Athlete",
        "",
        "Equipment from sport of choice, sweatband, powdered sports drink.",
    ),
    (
        "Skater",
        "",
        "Skateboard, video camera, bolt cutters.",
    ),
    (
        "Keyboard Warrior",
        "",
        "Laptop w/ bag, online following, fake credentials, energy drinks.",
    ),
    (
        "Volunteer Firefighter",
        "",
        "Collapsible ladder (bulky), axe (d6), fire extinguisher, flashlight.",
    ),
    (
        "Bicycle Courier",
        "",
        "Bike, helmet (+1 Armor), messenger bag, unopened package, multitool.",
    ),
    (
        "Bartender",
        "",
        "Barknife (d6), bottle of liquor, cigarettes, confiscated fake IDs.",
    ),
    (
        "Therapist",
        "",
        "Memo recorder, notebook and pen, business cards, small revolver (d6).",
    ),
    (
        "Administrative Assistant",
        "",
        "Extensive contacts, corporate credit card, expandable briefcase, taser (d6 DEX).",
    ),
    (
        "Actor",
        "",
        "Audition binder, portable charging brick, spare cosmetic supplies, change of clothes.",
    ),
    (
        "Engineer",
        "",
        "Laptop w/ design software, waterproof field notebook, wireless router, seldom used PPE.",
    ),
    (
        "Social Worker",
        "",
        "Laptop w/ bag, ID badge, pocket knife (d6), notebook and pen.",
    ),
    (
        "Teacher",
        "",
        "Coffee mug, scissors, large bag,",
    ),
    (
        "Contractor",
        "",
        "Stocked toolbelt, utility knife (d6), heavy duty flashlight, drill.",
    ),
)
archetypes_tuple = (
    archetype_data_base_game,
    archetype_data_the_bloom,
    archetype_data_hungry_hollow,
)
archetype_data = dict(zip(LIMINAL_HORROR_MODULES, archetypes_tuple))


ARCHETYPES = {
    module: [
        Archetype(name, des, take.split(", "))
        for name, des, take in archetype_data[module]
    ]
    for module in LIMINAL_HORROR_MODULES
}
