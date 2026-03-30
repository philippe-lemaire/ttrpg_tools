from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from .camp_events import camp_events_table
from crispy_forms.layout import Submit
from .twists import twists_data

camp_type_choices = [
    (table_name, table_name) for table_name in camp_events_table.keys()
]
danger_level_choices = [
    ("0", "Typical"),
    ("-1", "Unsafe"),
    ("-2", "Dangerous"),
]


class CampEventForm(forms.Form):
    table = forms.ChoiceField(label="Environmment", choices=camp_type_choices)
    survivalist_used_for_outdoor = forms.BooleanField(
        label="Survival skill used for outdoor camp", required=False
    )
    survivalist_used_for_concealment = forms.BooleanField(
        label="Survival skill used for concealment", required=False
    )
    ranger_present_outdoor_camp = forms.BooleanField(
        label="Ranger in the party (outdoor camp only)", required=False
    )
    outcast_present = forms.BooleanField(
        label="Outcast in the party (dwarven_made structure or dungeon camp only)",
        required=False,
    )
    set_watch = forms.BooleanField(label="The party has set a watch", required=False)
    bonus_from_past_event = forms.IntegerField(initial=0, required=False)

    danger_level = forms.ChoiceField(choices=danger_level_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("torchbearer:camp_events")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll event",
                css_class="m-1 btn-info",
            )
        )


twist_type_choice = [(twist_type, twist_type) for twist_type in twists_data.keys()]


class TwistForm(forms.Form):
    twist_type = forms.ChoiceField(label="Twist Type", choices=twist_type_choice)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("torchbearer:twists")
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll twist",
                css_class="m-1 btn-info",
            )
        )
