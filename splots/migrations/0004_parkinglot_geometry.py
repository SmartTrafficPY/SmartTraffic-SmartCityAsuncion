# Generated by Django 2.2.5 on 2019-09-30 13:23

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splots', '0003_auto_20190914_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinglot',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, default=None, null=True, srid=4326),
        ),
    ]
