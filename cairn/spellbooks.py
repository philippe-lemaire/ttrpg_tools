from dataclasses import dataclass


spellbook_data = [
    (
        "**Adhere**",
        "An object is covered in extremely sticky slime. _Adjacent objects stick to the book with great force._",
    ),
    (
        "**Anchor**",
        "A strong wire sprouts from your arms, affixing itself to two points within 50ft on each side. _If a rope is pulled through the iron loop on its spine, it becomes as heavy as an elephant._",
    ),
    (
        "**Animate Object**",
        "An object obeys your commands as best it can. _Moldable like clay. Childish laughter sprouts from its pages._",
    ),
    (
        "**Anthropomorphize**",
        "An animal either gains human intelligence or human appearance for one day. _Whimpers, purrs and growls depending on its treatment._",
    ),
    (
        "**Arcane Eye**",
        "You can see through a magical floating eyeball that flies around at your command. _Needs a spritz of water to open._",
    ),
    (
        "**Astral Prison**",
        "An object is frozen in time and space within an invulnerable crystal shell. _Silent, abstract, faces scream in anguish within._",
    ),
    (
        "**Attract**",
        "Two objects are strongly magnetically attracted to each other if they come within 10 feet. _Nearby compasses spin uselessly._",
    ),
    (
        "**Auditory Illusion**",
        "You create illusory sounds that seem to come from a direction of your choice. _Produces random and occasionally inopportune sounds throughout the day_.",
    ),
    (
        "**Babble**",
        "A creature must loudly and clearly repeat everything you think. It is otherwise mute. _When the text is read aloud, the words of others become unintelligible._",
    ),
    (
        "**Bait Flower**",
        "A plant sprouts from the ground that emanates the smell of decaying flesh. _Attracts flies._",
    ),
    (
        "**Beast Form**",
        "You and your possessions transform into a mundane animal. _Covered in thick fur, its edges lined with small teeth._",
    ),
    (
        "**Befuddle**",
        "A creature of your choice is unable to form new short-term memories for the duration of the spell. _Its contents shift and change each time it is opened._",
    ),
    (
        "**Body Swap**",
        "You switch bodies with a creature you touch. If one body dies, the other dies as well. _The front cover shows an image of the last creature to read it._",
    ),
    (
        "**Charm**",
        "A creature you can see treats you as a friend. _Warm to the touch, and smells of roses._",
    ),
    (
        "**Command**",
        "A target obeys a single three-word command that does not cause it harm. _Grows thinner over time, until finally disappearing forever._",
    ),
    (
        "**Comprehend**",
        "You become fluent in all languages for a short while. _Drips letters, staining whatever it touches._",
    ),
    (
        "**Cone of Foam**",
        "Dense foam sprays from your hand, coating the target. _Spongy and moist with a soapy residue._",
    ),
    (
        "**Control Plants**",
        "Nearby plants and trees obey you and gain the ability to move at a slow pace. _Leaves grow along the spine, and it smells faintly of decay._",
    ),
    (
        "**Control Weather**",
        "You may alter the type of weather at will, but you do not otherwise control it. _Highly resistant to fire and water damage._",
    ),
    (
        "**Cure Wounds**",
        "Restore 1d4 STR per day to a creature you can touch. _Smells of vinegar and thyme. Turns red after use._",
    ),
    (
        "**Deafen**",
        "All nearby creatures are deafened. _Nearby instruments occasionally sound off, as if in protest._",
    ),
    (
        "**Detect Magic**",
        "You can see or hear nearby magical auras. _Becomes warm to the touch if magic is used nearby._",
    ),
    (
        "**Disassemble**",
        "Any of your body parts may be detached and reattached at will, without causing pain or damage. You can still control them. _Regenerates any torn or defaced pages._",
    ),
    (
        "**Disguise**",
        "You may alter the appearance of one character at will as long as they remain humanoid. Attempts to duplicate other characters will seem uncanny. _The surface makes a perfect mirror._",
    ),
    (
        "**Displace**",
        "An object appears to be up to 15ft from its actual position. _Bits of string, clothing, and leaves are sometimes stuffed inside._",
    ),
    (
        "**Earthquake**",
        "The ground begins shaking violently. Structures may be damaged or collapse. _Sand dribbles from the corners, seemingly without stop._",
    ),
    (
        "**Elasticity**",
        "Your body can stretch up to 10ft. _Smells of taffy, and is very flexible._",
    ),
    (
        "**Elemental Wall**",
        "A straight wall of ice or fire 50ft long and 10ft high rises from the ground. _Skin and warmer substances stick to it after use._",
    ),
    (
        "**Filch**",
        "A visible item teleports to your hands. _An ally's prized possession may occasionally be found tucked between its covers_.",
    ),
    (
        "**Fish Lung**",
        "A target can breathe underwater until they surface again. _Smells strongly of the sea. Attracts wild animals._",
    ),
    (
        "**Flare**",
        "A bright ball of energy fires a trail of light into the sky, revealing your location to friend or foe. _Faintly glows in complete darkness_.",
    ),
    (
        "**Fog Cloud**",
        "A dense fog spreads out from you. _When submersed in water, the book eventually turns all the liquid to vapor._",
    ),
    (
        "**Frenzy**",
        "A nearby creature erupts in a frenzy of violence. _Rough, sandpaper cover that destroys any book it touches._",
    ),
    (
        "**Gate**",
        "A portal to a random plane opens. _A large hole is carved into the center, ending in a void. Items dropped within are never seen again_.",
    ),
    (
        "**Gravity Shift**",
        "You can change the direction of gravity, but only for yourself. _Attaches itself to the largest object nearby._",
    ),
    (
        "**Greed**",
        "A creature develops the overwhelming urge to possess a visible item of your choice. _The cover changes depending on the owner, subtly hinting at their deepest desires._",
    ),
    (
        "**Haste**",
        "Your movement speed is tripled. _Pages flip wildly while open. Can cause paper cuts._",
    ),
    (
        "**Hatred**",
        "A creature develops a deep hatred of another creature or group and wishes to destroy them. _Long term exposure to the book can cause suspicion, paranoia and distrust of others._",
    ),
    (
        "**Hear Whispers**",
        "You can hear faint sounds clearly. _The reader's voice is amplified for a short period of time afterwards._",
    ),
    (
        "**Hover**",
        "An object hovers, frictionless, 2ft above the ground. It can hold up to one humanoid. _Floats if dropped._",
    ),
    (
        "**Hypnotize**",
        "A creature enters a trance and will truthfully answer one yes or no question you ask it. _Eye-catching, swirling spirals don its covers._",
    ),
    (
        "**Icy Touch**",
        "A thick ice layer spreads across a touched surface, up to 10ft in radius. _Gloves required. Nonflammable_.",
    ),
    (
        "**Identify Owner**",
        "Letters appear over the object you touch, spelling out the name of the object’s owners, if there are any. _The book's interior lists the name of its previous owner._",
    ),
    (
        "**Illuminate**",
        "A floating light moves as you command. _When held in light, the pages become a prism of vibrant rainbows._",
    ),
    (
        "**Invisible Tether**",
        "Two objects within 10ft of each other cannot be moved more than 10ft apart. _Its pages are not attached by glue or thread, yet stay together nonetheless._",
    ),
    (
        "**Knock**",
        'A nearby mundane or magical lock unlocks loudly. _Locked. A new owner "produces" the key after their next meal._',
    ),
    ("**Leap**", "You jump up to 10ft high, once. _When thrown, it just keeps going._"),
    (
        "**Liquid Air**",
        "The air around you becomes swimmable. _Floats of its own volition, bouncing off of whatever it touches._",
    ),
    (
        "**Magic Dampener**",
        "All nearby magical effects have their effectiveness halved. _Relics within 100ft of the spellbook cannot be recharged._",
    ),
    (
        "**Manse**",
        "A sturdy, furnished cottage appears for hours. You can permit and forbid entry to it at will. _If left inside, both the book and the cottage vanish forever._",
    ),
    (
        "**Marble Craze**",
        "Your pockets are full of marbles and will refill every 30 seconds. _When jostled, makes a playful rattling sound._",
    ),
    (
        "**Masquerade**",
        "A character's appearance and voice becomes identical to those of a character you touch. _Extended use causes the owner to develop unconscious yet noticeable tics._",
    ),
    (
        "**Miniaturize**",
        "A creature you touch is shrunk down to the size of a mouse. _The text is ludicrously, comically large._",
    ),
    (
        "**Mirror Image**",
        "An illusory duplicate of yourself appears and is under your control. _Over time, the owner begins to question who is the original, and who is the duplicate._",
    ),
    (
        "**Mirrorwalk**",
        "A mirror becomes a gateway to another mirror that you looked into today. _Will not open unless the owner politely knocks on the cover._",
    ),
    (
        "**Multiarm**",
        "You temporarily gain an extra arm. _After use, the caster is wracked with phantom limb syndrome for a day._",
    ),
    (
        "**Night Sphere**",
        "A 50ft-wide sphere of darkness displaying the night sky appears before you. _Displays a prominent constellation on its cover_.",
    ),
    (
        "**Objectify**",
        "You become any inanimate object between the size of a grand piano and an apple. _The owner experiences intense pareidolia for days after use._",
    ),
    (
        "**Ooze Form**",
        "You become a living jelly. _Slowly drips an acid that eventually eats away anything it touches._",
    ),
    (
        "**Pacify**",
        "A creature near you has an aversion to violence. _Smells of jasmine and incense. Attracts children._",
    ),
    (
        "**Passage**",
        "Creates a temporary path through wood, stone or brick. _An object dropped on top of the book inevitably falls through the other side._",
    ),
    (
        "**Phobia**",
        "A nearby creature becomes terrified of an object of your choice. _Over time, haunting, abstract art begins to fill its pages._",
    ),
    (
        "**Pit**",
        "A pit 10ft wide and 10ft deep opens in the ground. _A standard piton can be safely stored in its spine_.",
    ),
    (
        "**Primal Surge**",
        "A creature rapidly evolves into a future version of its species. _The owner is haunted by strange visions of their own ancestors._",
    ),
    (
        "**Push/Pull**",
        "An object of any size is pulled directly towards you or pushed directly away from you with the strength of one man. _Any force against the book is comically amplified._",
    ),
    (
        "**Raise Dead**",
        "A skeleton rises from the ground to serve you. They are incredibly stupid and can only obey simple orders. _The owner becomes more and more fascinated with bones after each use._",
    ),
    (
        "**Raise Spirit**",
        "The spirit of a nearby corpse manifests and will answer 1 question. _The answers (but not their questions) are forever inscribed in its pages._",
    ),
    (
        "**Read Mind**",
        "You can hear the surface thoughts of nearby creatures. _Long-term possession can cause the reader to mistake the thoughts of others as their own._",
    ),
    (
        "**Repel**",
        "Two objects are strongly magnetically repelled from each other within 10 feet. _Closed by two powerful straps that spring open at inopportune times._",
    ),
    (
        "**Scry**",
        "You can see through the eyes of a creature you touched earlier today. _The owner's eyes turn milky-white for an hour after use._",
    ),
    (
        "**Sculpt Elements**",
        "Inanimate material behaves like clay in your hands. _Slowly decays on contact with wood or cloth. Bury in dirt or submerge in water to refresh._",
    ),
    (
        "**Sense**",
        "Choose one kind of object (key, gold, arrow, jug, etc). You can sense the nearest example. _The book's previous owner is always aware of the book's current location._",
    ),
    (
        "**Shield**",
        "A creature you touch is protected from mundane attacks for one minute. _Bound in rusty ring-mail and is quite heavy. If held, provides +1 Armor._",
    ),
    (
        "**Shroud**",
        "A creature you touch is invisible until they move. _Invisible to any but the book's current owner._",
    ),
    (
        "**Shuffle**",
        "Two creatures you can see instantly switch places. _If stolen but not yet read, it reappears wherever its owner last left it._",
    ),
    (
        "**Skillful Repair**",
        "You make minor repairs to a nonliving object. _Sewn from the vellum of one hundred books, no two pages are alike._",
    ),
    (
        "**Sleep**",
        "A creature you can see falls into a light sleep. _Soft as a pillow, but yields only fitful sleep._",
    ),
    (
        "**Slick**",
        "Every surface in a 30ft radius becomes extremely slippery. _Gloves are required for handling, lest the book is dropped in a most comical fashion._",
    ),
    (
        "**Smoke Form**",
        "Your body becomes a living smoke that you can control. _Smells of campfire. The pages cannot be burnt, but are very sensitive to moisture._",
    ),
    (
        "**Sniff**",
        "You can smell even the faintest traces of scents. _Expresses a strong odor detectable only by its owner._",
    ),
    (
        "**Snuff**",
        "The source of any mundane light you can see is instantly snuffed out. _If left in one place for long periods, nearby light sources eventually dim, then finally go out._",
    ),
    (
        "**Sort**",
        "Inanimate items sort themselves according to categories you set. _Rights itself when dropped or thrown._",
    ),
    (
        "**Spellsaw**",
        "A whirling blade flies from your chest, clearing any plant material in its way. It is otherwise harmless. _Wrapped in stained leather, it should be oiled at least once a month_.",
    ),
    (
        "**Spider Climb**",
        "You can climb surfaces like a spider. _New cobwebs must be pushed aside prior to each use. They are hard to remove._",
    ),
    (
        "**Swarm**",
        "You become a swarm of crows, rats, or piranhas. You can only be harmed by _blast_ attacks. _Easily broken into a dozen distinct parts that slowly move towards one another over time._",
    ),
    (
        "**Target Lure**",
        "An object you touch becomes the target of any nearby spell. _Attracts all manner of magical creatures, spell leaks, and scrying._",
    ),
    (
        "**Telekinesis**",
        "You may mentally 1 move item under 60lbs. _The owner can summon the book through mental command alone (WIL save or become deprived afterwards)._",
    ),
    (
        "**Telepathy**",
        "Two creatures can hear each other’s thoughts, no matter how far apart. _The holder can hear (but not respond) to the thoughts of whoever last possessed it, and vice versa._",
    ),
    (
        "**Teleport**",
        "An object or person you can see is transported from one place to another in a 50ft radius. _Can be destroyed to create a portal to another dimension._",
    ),
    (
        "**Thicket**",
        "A thicket of trees and dense brush up to 50ft wide suddenly sprouts up. _Wrapped in vines that must be destroyed again with each use._",
    ),
    (
        "**Time Control**",
        "Time in a 50ft bubble slows down or increases by 10% for 30 seconds. _Alternates its appearance as either impossibly old or freshly written._",
    ),
    (
        "**True Sight**",
        "You see through all nearby illusions. _Cannot be concealed by magic, and sticks out like a sore thumb._",
    ),
    (
        "**Upwell**",
        "A spring of seawater appears. _Hardened leather bindings caked in salt and living barnacles._",
    ),
    (
        "**Vision**",
        "You completely control what a creature sees. _An unnerving, lidless eye graces the front cover._",
    ),
    (
        "**Visual Illusion**",
        "A silent, immobile, room-sized illusion of your choice appears. _Filled with rich, colorful pages very much like a children's bedtime story._",
    ),
    (
        "**Ward**",
        "A silver circle 50ft across appears on the ground. Choose one species that cannot cross it. _The covers are decorated with bizarre, otherworldly creatures with thousands of eyes._",
    ),
    (
        "**Web**",
        "Your wrists shoot thick webbing. _The text is alien, yet somehow intelligible, for it is the language of dreams._",
    ),
    (
        "**Widget**",
        "A primitive version of a drawn tool or item appears before you and disappears after a short time. _Smells of iron and rust, sweat and effort. Faint sounds of harsh labor emanate from deep within its pages._",
    ),
    (
        "**Wizard Mark**",
        "Your finger can shoot a stream of ulfire-colored paint. This paint is only visible to you and can be seen at any distance, even through solid objects. _Inside the front cover is a small pocket containing a thin pad of paper, listing the name and date of death of all previous owners._",
    ),
    ("**X-Ray Vision**", "**X-Ray Vision**"),
]


@dataclass
class Spellbook:
    name: str
    description: str

    def __repr__(self):
        display_name = self.name.replace("<p>", "").replace("</p>", "")
        display_description = self.description.replace("<p>", "").replace("</p>", "")

        return f"{display_name}: {display_description}."


spellbooks = [Spellbook(name, description) for name, description in spellbook_data]
