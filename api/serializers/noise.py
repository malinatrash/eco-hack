from rest_framework import serializers

from api.models import Noise


class NoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noise
        fields = ['id', 'latitude', 'longitude', 'decibels', 'frequency', 'datetime']
