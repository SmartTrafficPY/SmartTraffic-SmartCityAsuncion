# Generated by Django 2.2.5 on 2019-12-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uccarpool', '0009_itineraryroute_agg_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itineraryroute',
            old_name='agg_cost',
            new_name='aggCost',
        ),
    ]