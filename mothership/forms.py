from django import forms
from .character import classes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from .search_tables import MODULES


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


class ModuleSelectionForm(forms.Form):
    choices = [(c, c) for c in MODULES.keys()]
    module_choice = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "mothership:search_tables"

        self.helper.add_input(
            Submit(
                "submit",
                "Next",
                css_class="m-1 btn-secondary",
            )
        )
