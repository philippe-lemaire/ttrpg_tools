from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class LevelForm(forms.Form):
    choices = [(k, k) for k in range(1, 6)]
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
