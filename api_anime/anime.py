from .models import Anime 
from django import forms

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ('title', 'image_url', 'score', 'episodes', 'synopsis', 'type')