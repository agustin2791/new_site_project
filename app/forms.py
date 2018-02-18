from django import forms
from django.forms import Form, ModelForm, ModelChoiceField, ModelMultipleChoiceField, HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden, Field, Button, Fieldset, Div
from crispy_forms.bootstrap import FormActions, AppendedText, FieldWithButtons, StrictButton
from crispy_forms.bootstrap import TabHolder, Tab, InlineField
import models

class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        self.helper.form_id = 'id_new_event'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field('event_name'),
            Field('date'),
            Field('date_end'),
            Field('time_start'),
            Field('end_time'),
            Field('host'),
            Field('location'),
            Field('city'),
            Field('state'),
            Field('zip_code'),
            Field('guests'),
            Field('description'),
            Field('template'),
            FormActions(
                Submit('new_event_save', 'Submit', css_class='btn btn-primary')
            )
        )

        super(EventForm, self).__init__(*args, **kwargs)

        def save(self, *args, **kwargs):
            cleaned_data = self.cleaned_data
            saved_form = super(EventForm, self).save(*args, **kwargs)

            # if host:
            #     event_host = models.UserProfile.objects.get(id=host)
            #     saved_form.host = event_host

    class Meta:
        model = models.Event
        exclude = []
