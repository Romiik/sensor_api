from django.db import models


class SoilTemperature(models.Model):

    value = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Soil Temperature'


class AirTemperature(models.Model):

    value = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Air Temperature'


class Humidity(models.Model):

    value = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Humidity'


class SoilMoistureLevel(models.Model):

    value = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Soil Moisture Level'


class Sunlight(models.Model):

    value = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sunlight'
