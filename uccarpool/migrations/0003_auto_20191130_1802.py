# Generated by Django 2.2.5 on 2019-11-30 18:02

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uccarpool', '0002_carpool_carpoolitinerary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpoolitinerary',
            name='geopoints',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.gis.db.models.fields.PointField(
                    blank=True, null=True, srid=4326), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='carpoolitinerary',
            name='timestamps',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.DateTimeField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
