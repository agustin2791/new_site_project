from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import models

class NewEventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper(self)

        self.helper.form_id = 'id_new_event'
        self.helper.form_class = 'well'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('event_name'),
            Fieldset('date'),
            Fieldset('date_end'),
            Fieldset('time_start'),
            Fieldset('end_time'),
            Fieldset('location'),
            Fieldset('city'),
            Fieldset('state'),
            Fieldset('zip_code'),
            Fieldset('guests'),
            Fieldset('description'),
            Fieldset('template'),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )

        super(NewEventForm, self).__init__(*args, **kwargs)
        class Meta:
            model = models.NewEvent
