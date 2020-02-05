# Generated by Django 2.2.4 on 2019-10-24 17:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smreports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='value',
            field=models.BooleanField(
                help_text='True if the contribution is confirmed or False if the contribution is solved'),
        ),
    ]
