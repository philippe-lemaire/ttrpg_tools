from django import forms
from .character import classes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class ClassesForm(forms.Form):
    choices = [(c, c) for c in classes]
    class_choice = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "mothership:create_character_step_2"

        self.helper.add_input(
            Submit(
                "submit",
                "Next",
                css_class="m-1 btn-secondary",
            )
        )
