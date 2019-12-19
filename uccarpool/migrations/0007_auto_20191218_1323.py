# Generated by Django 2.2.5 on 2019-12-18 13:23

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uccarpool', '0006_auto_20191216_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', django.contrib.postgres.fields.ArrayField(
                    base_field=models.IntegerField(blank=True, null=True),
                    blank=True,
                    default=list,
                    null=True,
                    size=None)
                 ),
                ('timestamps', django.contrib.postgres.fields.ArrayField(
                    base_field=models.DateTimeField(blank=True, null=True), blank=True, null=True, size=None)),
                ('itinerary', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uccarpool.UserItinerary')),
            ],
            options={
                'verbose_name_plural': 'Itinerary Routes',
            },
        ),
        migrations.AlterField(
            model_name='carpool',
            name='route',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uccarpool.ItineraryRoute'),
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]