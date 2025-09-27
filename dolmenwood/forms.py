from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .gamelogic.encounters import Encounter
from .gamelogic.constants import REGIONS, ENCOUNTER_CIRCUMSTANCES


class EncounterForm(forms.Form):
    situation_choices = [(c, c) for c in ENCOUNTER_CIRCUMSTANCES]
    situation = forms.ChoiceField(choices=situation_choices)
    region_choices = [(r, r) for r in REGIONS]
    region = forms.ChoiceField(choices=region_choices, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "dolmenwood:roll_encounters"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll encounter",
                css_class="m-1 btn-secondary",
            )
        )
