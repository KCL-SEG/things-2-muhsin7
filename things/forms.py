from django import forms
"""Forms of the project."""

# Create your forms here.
class ThingsForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    quantity = forms.IntegerField(widget=forms.NumberInput())
