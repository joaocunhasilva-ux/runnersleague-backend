from rest_framework import serializers
from .models import Athlete, Club, Race, Result

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = "__all__"

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"
