from rest_framework import serializers 
from .models import User, Anime, Character


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
        
class CharacterSerializer(serializers.Serializer):
    class Meta:
        model = Character
        fields = '__all__'
        
class AnimeSerializer(serializers.Serializer):
    class Meta:
        model = Anime
        fields = '__all__'
    