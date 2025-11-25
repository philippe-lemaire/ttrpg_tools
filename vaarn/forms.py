from django import forms
from .game_logic.ancestries import ANCESTRIES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class AncestryForm(forms.Form):
    choices = [(ancestry, ancestry) for ancestry in ANCESTRIES]
    ancestry = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "vaarn:character_generator_with_ancestry"

        self.helper.add_input(
            Submit(
                "submit",
                "Generate",
                css_class="m-1 btn-secondary",
            )
        )


class FollowerForm(forms.Form):
    ego = forms.IntegerField(
        max_value=10,
        min_value=1,
        required=True,
        initial=1,
        label="EGO score of main PC",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "vaarn:generate_follower"

        self.helper.add_input(
            Submit(
                "submit",
                "Generate",
                css_class="m-1 btn-secondary",
            )
        )
