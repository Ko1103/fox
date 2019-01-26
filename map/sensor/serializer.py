from rest_framework import serializers
from .models import Sensor, Reference

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('sensor_name', 'value', 'created_at')

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('sensor_name', 'value', 'temp_value', 'create_at')