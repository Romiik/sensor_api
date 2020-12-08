from django.shortcuts import render
from .models import SoilTemperature, AirTemperature, SoilMoistureLevel, Humidity, Sunlight
from .serializers import SoilTemperatureSerializer, SoilMoistureLevelSerializer, AirTemperatureSerializer, HumiditySerializer, SunlightSerializer
from rest_framework import viewsets


class SoilTemperatureViewSet(viewsets.ModelViewSet):

    serializer_class = SoilTemperatureSerializer
    queryset = SoilTemperature.objects.all()


class SoilMoistureLevelViewSet(viewsets.ModelViewSet):

    serializer_class = SoilMoistureLevelSerializer
    queryset = SoilMoistureLevel.objects.all()


class AirTemperatureViewSet(viewsets.ModelViewSet):

    serializer_class = AirTemperatureSerializer
    queryset = AirTemperature.objects.all()


class HumidityViewSet(viewsets.ModelViewSet):

    serializer_class = HumiditySerializer
    queryset = Humidity.objects.all()


class SunlightViewSet(viewsets.ModelViewSet):

    serializer_class = SunlightSerializer
    queryset = Sunlight.objects.all()
