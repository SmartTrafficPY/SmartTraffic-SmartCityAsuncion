# Generated by Django 2.2.5 on 2019-11-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucarpoolingpersonalitytraittype',
            name='weight',
            field=models.FloatField(),
        ),
    ]
