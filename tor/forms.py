from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .tor_dice_roller import roller
from crispy_forms.layout import Submit


class ActionResolutionForm(forms.Form):
    rating = forms.IntegerField(
        max_value=8, min_value=0, initial=0, label="Success Dice (rating + bonus dice)"
    )
    target_number = forms.IntegerField(max_value=25, min_value=8, initial=15)
    favoured = forms.BooleanField(required=False, initial=False)
    ill_favoured = forms.BooleanField(required=False, initial=False)
    weary = forms.BooleanField(required=False, initial=False)
    miserable = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("tor:action_resolution")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll",
                css_class="btn btn-primary mt-3",
            )
        )


class TreasureForm(forms.Form):
    choices = [(1, "Lesser"), (2, "Greater"), (3, "Marvellous")]
    hoard_rating = forms.ChoiceField(choices=choices)
    suggest_magical_treasure = forms.BooleanField(
        label="Roll Magical Treasure Blessings", required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("tor:treasure")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll",
                css_class="btn btn-primary mt-3",
            )
        )


class StriderTellingTableForm(forms.Form):
    choices = [
        (1, "Certain"),
        (2, "Likely"),
        (3, "Middling"),
        (4, "Doubtful"),
        (5, "Unthinkable"),
    ]
    chance = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("tor:strider_telling_table")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Ask the Telling Table",
                css_class="btn btn-primary mt-3",
            )
        )


class FortuneTableForm(forms.Form):
    choices = [(1, "Fortune"), (2, "Ill-Fortune")]
    table = forms.ChoiceField(choices=choices, label="Chose your table")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("tor:strider_fortune_table")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Ask the Fortune Tables",
                css_class="btn btn-primary mt-3",
            )
        )


class StriderJourneyEventsForm(forms.Form):
    choices = [
        (1, "Border Land (Favoured Roll)"),
        (2, "Wild Land"),
        (3, "Dark Land (Ill-favoured Roll)"),
    ]
    land = forms.ChoiceField(
        choices=choices,
        label="What type of Land is the Hex the event is taking place in?",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("tor:strider_solo_journey")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Solo Journey Event Roll",
                css_class="btn btn-primary mt-3",
            )
        )


class RevelationEpisodeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("tor:strider_revelation_episode")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll Revelation Episode",
                css_class="btn btn-primary mt-3",
            )
        )
