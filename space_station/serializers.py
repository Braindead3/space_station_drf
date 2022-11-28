from .models import Station, Instructions
from rest_framework import serializers


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'state', 'created_at', 'destroyed_time']
        read_only_fields = ('id', 'state', 'created_at', 'destroyed_time')


class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ['user', 'station', 'axis', 'distance']
