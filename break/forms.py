from django import forms
from .callings import CALLINGS
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class CallingForm(forms.Form):
    choices = [(n, n.upper()) for n in list(CALLINGS.keys())]
    calling = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "break:character_creation"

        self.helper.add_input(
            Submit(
                "submit",
                "Confirm Calling",
                css_class="m-1 btn-secondary",
            )
        )
