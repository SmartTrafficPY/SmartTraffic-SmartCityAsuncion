# Generated by Django 2.2.2 on 2019-06-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sp_profiles", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Sp_profiles",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=50)),
                ("alias", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(name="Perfil_SmartParking"),
    ]
