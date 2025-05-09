from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .spark_tables import spark_tables
from crispy_forms.layout import Submit

spark_table_choices = [(table_name, table_name) for table_name in spark_tables.keys()]


class SparkForm(forms.Form):
    table = forms.ChoiceField(choices=spark_table_choices)

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
