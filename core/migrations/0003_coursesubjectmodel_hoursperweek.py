# Generated by Django 5.2 on 2025-05-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_coursesubjectmodel_hoursperweek"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursesubjectmodel",
            name="hoursPerWeek",
            field=models.TimeField(default="00:00:00"),
        ),
    ]
