from django import forms
from .encounters_per_floor import encounters_per_floor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Monarch


class FloorForm(forms.Form):
    choices = [
        (k, encounters_per_floor[k].get("name").upper())
        for k in encounters_per_floor.keys()
    ]
    floor = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "gradientdescent:roll_encounters"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll encounter",
                css_class="m-1 btn-secondary",
            )
        )


class MonarchForm(forms.ModelForm):
    class Meta:
        model = Monarch
        fields = ["current_stress"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Update Monarch",
                css_class="m-1 btn-secondary",
            )
        )
