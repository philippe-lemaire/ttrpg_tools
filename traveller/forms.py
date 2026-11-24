from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TravellerRollForm(forms.Form):
    characteristic_dm = forms.IntegerField(
        min_value=-3, max_value=3, initial=0, required=True, label="Characteristic DM"
    )
    skill_dm = forms.IntegerField(
        min_value=-3,
        max_value=6,
        initial=0,
        required=True,
        label="Skill DM, set at -3 if untrained in the Skill",
    )

    difficulty_values = {
        "Simple": 2,
        "Easy": 4,
        "Routine": 6,
        "Average": 8,
        "Difficult": 10,
        "Very Difficult": 12,
        "Formidable": 14,
        "Impossible": 16,
    }

    difficulty_values = {v: k for k, v in difficulty_values.items()}
    difficulty = forms.ChoiceField(choices=difficulty_values.items(), initial=8)
    boon_bane = forms.ChoiceField(
        choices=[("none", "Default"), ("boon", "Boon"), ("bane", "Bane")],
        initial="none",
        label="Boon or Bane",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("traveller:roll")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll",
                css_class="m-1 btn-info",
            )
        )


class TravellerWorldProfileForm(forms.Form):
    profile = forms.CharField(
        label="World Profile",
        max_length=9,
        widget=forms.TextInput(attrs={"placeholder": "D9A6777-4"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("traveller:describe_world")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll",
                css_class="m-1 btn-info",
            )
        )
