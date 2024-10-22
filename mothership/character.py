from dataclasses import dataclass


@dataclass
class Character:
    strength: int
    speed: int
    intellect: int
    combat: int
    sanity: int
    fear: int
    body: int
    class_: str
    max_wounds: int
    wounds: int
    health: int
    max_health: int
    stress: int
    minimum_stress: int
    trauma_response: str
    skills: list
    trinket: str
    patch: str
    equipment: list
    credits: int
    portrait: str
    name: str
    pronouns: str

    def update_stats(self):
        class_ = self.class_
        if class_ == "Marine":
            self.combat += 10
            self.body += 10
            self.fear += 20
            self.max_wounds += 1

        if class_ == "Android":
            # TODO -10 to 1 stat > form
            self.intellect += 20
            self.fear += 60
            self.max_wounds += 1
        if class_ == "Scientist":
            self.intellect += 10
            # TODO +5 to 1 stat > form
            self.sanity += 30
        if class_ == "Teamster":
            self.strength += 5
            self.speed += 5
            self.intellect += 5
            self.combat += 5
            self.sanity += 10
            self.fear += 10
            self.body += 10


classes = ("Marine", "Android", "Scientist", "Teamster")

classes_descriptions = (
    "+10 Combat<br>+10 Body Save<br>+20 Fear Save<br>+1 max Wounds",
    "+20 Intellect<br>-10 to 1 Stat<br>+60 Fear Save<br>+1 max Wounds",
    "+10 Intellect<br>+5 to 1 Stat<br>+30 Sanity Save",
    "+5 to all Stats<br>+10 to all Saves",
)
trauma_responses = (
    "WHENEVER YOU PANIC, EVERY CLOSE FRIENDLY PLAYER MUST MAKE A FEAR SAVE.",
    "FEAR SAVES MADE BY CLOSE FRIENDLY PLAYERS ARE AT DISADVANTAGE.",
    "WHENEVER YOU FAIL A SANITY SAVE, ALL CLOSE FRIENDLY PLAYERS GAIN 1 STRESS.",
    "ONCE PER SESSION, YOU MAY TAKE ADVANTAGE ON A PANIC CHECK.",
)
classes_descriptions_d = dict(zip(classes, zip(classes_descriptions, trauma_responses)))
