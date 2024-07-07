from django import forms
class todos(forms.Form):
    name = forms.CharField(max_length=100)
class updater(forms.Form):
    new_value = forms.CharField(max_length=100)
