from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .characters import abilities, stat_arrays


class CharacterCreationForm(forms.Form):
    stat_array_choices = [(k, str(v)) for k, v in stat_arrays.items()]
    stat_array_nb = forms.ChoiceField(
        choices=stat_array_choices,
        label="Choose your base ability scores (STR, DEX, INT)",
    )
    ability_choices = [(a, a) for a in abilities]
    ability_to_raise = forms.ChoiceField(
        choices=ability_choices, label="Choose an ability to be raised by 1d6"
    )
    gender = forms.ChoiceField(choices=[(g, g) for g in ("Male", "Female")])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "addg:character_generator"

        self.helper.add_input(
            Submit(
                "submit",
                "Submit",
                css_class="m-1 btn-secondary",
            )
        )
