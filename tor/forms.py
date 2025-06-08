from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .tor_dice_roller import roller
from crispy_forms.layout import Submit


class ActionResolutionForm(forms.Form):
    rating = forms.IntegerField(max_value=5, min_value=0, initial=0)
    target_number = forms.IntegerField(max_value=18, min_value=10, initial=15)
    favored = forms.BooleanField(required=False, initial=False)
    ill_favored = forms.BooleanField(required=False, initial=False)
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
