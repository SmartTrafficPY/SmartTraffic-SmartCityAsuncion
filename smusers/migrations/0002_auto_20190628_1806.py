# Generated by Django 2.2.2 on 2019-06-28 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("smusers", "0001_initial")]

    operations = [migrations.RenameField(model_name="user", old_name="last_name", new_name="lastname")]
