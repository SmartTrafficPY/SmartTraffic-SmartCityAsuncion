# Generated by Django 2.2.4 on 2019-10-24 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smreports', '0002_auto_20191024_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportpoi',
            old_name='report_name',
            new_name='report_type',
        ),
    ]