from django.urls import path, include
from .views import SoilTemperatureViewSet, SoilMoistureLevelViewSet, AirTemperatureViewSet, HumidityViewSet, SunlightViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('soil_temperature', SoilTemperatureViewSet,
                basename='soil_temperature')
router.register('air_temperature', AirTemperatureViewSet,
                basename='air_temperatue')
router.register('soil_moisture_level',
                SoilMoistureLevelViewSet, basename='soil_moisture_level')
router.register('humidity', HumidityViewSet, basename='humidity')
router.register('sunlight', SunlightViewSet, basename='sunlight')


urlpatterns = [
    path('', include(router.urls)),
]
