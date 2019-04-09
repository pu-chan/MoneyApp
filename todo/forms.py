from django import forms

class CheckForm(forms.Form):
    is_competed = forms.BooleanField(label='check', required=False)
