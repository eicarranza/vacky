""" Farm forms """

# Django
from django import forms

# Models
from vacky.farms.models import Farm

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ('name', 'address')