from .models import Character
from django import forms

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'