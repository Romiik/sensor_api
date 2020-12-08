from rest_framework import serializers
from .models import SoilTemperature, SoilMoistureLevel, Sunlight, AirTemperature, Humidity


class SoilTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilTemperature
        fields = '__all__'


class SoilMoistureLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilMoistureLevel
        fields = '__all__'


class AirTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirTemperature
        fields = '__all__'


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = '__all__'


class SunlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunlight
        fields = '__all__'
