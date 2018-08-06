from django import forms

class RecordLocationForm(forms.Form):
    record_id = forms.IntegerField()
    place_id = forms.IntegerField()