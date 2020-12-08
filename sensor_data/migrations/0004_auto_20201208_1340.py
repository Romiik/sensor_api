# Generated by Django 3.1.4 on 2020-12-08 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data', '0003_sunlight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airtemperature',
            options={'verbose_name_plural': 'Air Temperature'},
        ),
        migrations.AlterModelOptions(
            name='humidity',
            options={'verbose_name_plural': 'Humidity'},
        ),
        migrations.AlterModelOptions(
            name='soilmoisturelevel',
            options={'verbose_name_plural': 'Soil Moisture Level'},
        ),
        migrations.AlterModelOptions(
            name='soiltemperature',
            options={'verbose_name_plural': 'Soil Temperature'},
        ),
        migrations.AlterModelOptions(
            name='sunlight',
            options={'verbose_name_plural': 'Sunlight'},
        ),
    ]