# Generated by Django 3.1.4 on 2020-12-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoilTemperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]