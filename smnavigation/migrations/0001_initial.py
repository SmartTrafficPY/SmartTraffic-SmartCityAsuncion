# Generated by Django 2.2.4 on 2020-01-04 18:05

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('destination', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('finished', models.BooleanField(help_text="true if user finished the navigation, false if didn't")),
                ('score', models.IntegerField(
                    choices=[(1, 1), (2, 2), (3, 3), (4, 4)],
                    help_text='1 lowest score, 5 highest score',
                    null=True)),
                ('user_requested',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]