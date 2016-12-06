# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20161130_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='nearest_busstop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BusStop'),
        ),
        migrations.AddField(
            model_name='location',
            name='nearest_trainstop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TrainStop'),
        ),
    ]