from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RollForm(forms.Form):
    dice = forms.IntegerField(min_value=0, max_value=6, initial=0)
    thorns = forms.IntegerField(min_value=0, max_value=3, initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "grimwild:grimwild_roll"

        self.helper.add_input(
            Submit(
                "submit",
                "Generate",
                css_class="m-1 btn-secondary",
            )
        )
