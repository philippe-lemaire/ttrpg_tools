from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .spark_tables import spark_tables_by_theme
from crispy_forms.layout import Submit


class SparkThemeForm(forms.Form):
    theme = forms.ChoiceField(
        choices=[(choice, choice) for choice in spark_tables_by_theme.keys()]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("mythic_bastionland:spark_tables")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll sparks",
                css_class="m-1 btn-info",
            )
        )
