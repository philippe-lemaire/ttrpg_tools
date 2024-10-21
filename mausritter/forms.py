from django import forms


class TreasureForm(forms.Form):
    location = forms.BooleanField(
        label="Êtes-vous dans un ancienne colonie de souris, un château ou un dungeon ?",
        required=False,
    )
    magical = forms.BooleanField(
        label="Êtes-vous dans un lieu chargé de magie ?",
        required=False,
    )
    beast = forms.BooleanField(
        label="Le trésor était-il défendu par une grande créature, ou un piège sournois ?",
        required=False,
    )
    adversity = forms.BooleanField(
        label="Les souris ont-elle dû affronter de grands périls pour obtenir ce trésor ?",
        required=False,
    )


class RollSpellForm(forms.Form):
    n_dice = forms.IntegerField(
        label="À quelle puissance lancer le sort (de 1 à 3) ?",
        required=True,
        min_value=1,
        max_value=3,
    )
