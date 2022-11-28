from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator

"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea(), max_length=120)
    quantity = forms.IntegerField(widget=forms.NumberInput(), validators=[MinValueValidator(0),MaxValueValidator(50)])
