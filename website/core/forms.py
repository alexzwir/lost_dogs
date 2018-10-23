from django import forms

class LostPetPointForm(forms.Form):
    local = forms.CharField()