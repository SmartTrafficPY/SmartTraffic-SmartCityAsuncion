# Generated by Django 2.2.5 on 2019-09-10 22:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("smevents", "0003_auto_20190910_2218")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="extra_information",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        )
    ]
