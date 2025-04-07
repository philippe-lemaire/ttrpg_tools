from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .archetypes import ARCHETYPES
from crispy_forms.layout import Submit

module_choices = [(table_name, table_name) for table_name in ARCHETYPES.keys()]


class ModuleForm(forms.Form):
    module = forms.ChoiceField(choices=module_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("liminal_horror:generate_character")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll character",
                css_class="mt-3 mb-3 btn-warning",
            )
        )
