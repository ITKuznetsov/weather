from rest_framework import serializers
from weather.models import SearchHistory

class CityCountSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    count = serializers.IntegerField()