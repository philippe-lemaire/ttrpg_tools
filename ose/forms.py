from django import forms


class AdventuringPartyForm(forms.Form):
    level = forms.ChoiceField(
        choices=[(1, "Basic"), (2, "Expert")], required=True, label="Party Level"
    )


class DeckofManyThingsForm(forms.Form):
    ncards = forms.IntegerField(
        min_value=1, max_value=4, label="How many cards do you want to draw?"
    )


class HereticGnomesForm(forms.Form):
    ngnomes = forms.IntegerField(
        min_value=1, max_value=20, label="How many gnomes do you need?"
    )
