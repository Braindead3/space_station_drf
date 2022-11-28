from .models import Station, Instructions
from rest_framework import serializers


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'state', 'created_at', 'destroyed_time']
        read_only_fields = ('id', 'state', 'created_at', 'destroyed_time')


class InstructionsSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        if self.is_valid():
            instruction = Instructions(user=self.validated_data['user'],
                                       station=self.validated_data['station'],
                                       axis=self.validated_data['axis'],
                                       distance=self.validated_data['distance'])
            instruction.save()
            return instruction
        else:
            return self.errors

    class Meta:
        model = Instructions
        fields = ['user', 'station', 'axis', 'distance']
