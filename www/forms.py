from django import forms

class RecordLocationForm(forms.Form):
    record_id = forms.IntegerField(disabled=True)
    place_id = forms.IntegerField(disabled=True)