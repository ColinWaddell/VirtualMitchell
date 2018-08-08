from django import forms

from .utilities import record_update_with_location

class RecordLocationForm(forms.Form):
    record_id = forms.IntegerField()
    place_id = forms.IntegerField()

    def update_location(self):
        record_id = self.cleaned_data['record_id']
        place_id = self.cleaned_data['place_id']
        record_update_with_location(record_id, place_id)