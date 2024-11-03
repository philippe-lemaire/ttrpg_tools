from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from .land_of_cicada_encounters import regions, cloud_empress_encounters


class LevelForm(forms.Form):
    choices = [(k, k) for k in range(6)]
    level = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "cloudempress:roll_cavern"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll Cavern",
                css_class="m-1 btn-secondary",
            )
        )


class RegionSelectForm(forms.Form):
    choices = [(r, r) for r in regions]
    region = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "cloudempress:roll_encounter_land_of_cicadas"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll Encounter",
                css_class="m-1 btn-secondary",
            )
        )
