from django import forms
from django.urls import reverse
from .game_facts import classes, ancestries, backgrounds
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ClassChoiceForm(forms.Form):
    ancestry_choice_field = [
        (k, cl) for k, cl in zip(range(len(ancestries)), ancestries)
    ]
    ancestry = forms.ChoiceField(choices=ancestry_choice_field, required=True)
    background_choice_field = [
        (k, ": ".join(background))
        for k, background in zip(range(len(backgrounds)), backgrounds)
    ]
    background = forms.ChoiceField(choices=background_choice_field, required=True)
    class_choice_field = [(k, cl) for k, cl in zip(range(len(classes)), classes)]
    class_ = forms.ChoiceField(choices=class_choice_field, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "create_pc"
        self.helper.add_input(Submit("submit", "Create PC"))


class WizardSpellCastingForm(forms.Form):
    bonus = forms.IntegerField(min_value=-5, max_value=10)
    spell_tier = forms.IntegerField(min_value=1, max_value=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("shadowdark:cast_wizard_spell")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Cast!",
                css_class="mt-2 btn-warning",
            )
        )
