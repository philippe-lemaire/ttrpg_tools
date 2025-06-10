from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .tor_dice_roller import roller
from crispy_forms.layout import Submit


class ActionResolutionForm(forms.Form):
    rating = forms.IntegerField(max_value=6, min_value=0, initial=0)
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
    rating = forms.ChoiceField(choices=choices)

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
