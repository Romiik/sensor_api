from django.contrib import admin
from .models import SoilTemperature, AirTemperature, Sunlight, Humidity, SoilMoistureLevel
# Register your models here.


class SoilTemperatureAdmin(admin.ModelAdmin):
    search_fields = ('date', 'time')
    list_display = ['value', 'date', 'time']


class AirTemperatureAdmin(admin.ModelAdmin):
    search_fields = ('date', 'time')
    list_display = ['value', 'date', 'time']


class HumidityAdmin(admin.ModelAdmin):
    search_fields = ('date', 'time')
    list_display = ['value', 'date', 'time']


class SoilMoistureLevelAdmin(admin.ModelAdmin):
    search_fields = ('date', 'time')
    list_display = ['value', 'date', 'time']


class SunlightAdmin(admin.ModelAdmin):
    search_fields = ('date', 'time')
    list_display = ['value', 'date', 'time']


admin.site.register(SoilTemperature, SoilTemperatureAdmin)
admin.site.register(AirTemperature, AirTemperatureAdmin)
admin.site.register(SoilMoistureLevel, SoilMoistureLevelAdmin)
admin.site.register(Humidity, HumidityAdmin)
admin.site.register(Sunlight, SunlightAdmin)
