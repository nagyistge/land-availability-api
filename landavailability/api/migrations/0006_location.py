# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 12:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_merge_20161124_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('authority', models.CharField(blank=True, max_length=255, null=True)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('uprn', models.CharField(blank=True, max_length=100, null=True)),
                ('unique_asset_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]