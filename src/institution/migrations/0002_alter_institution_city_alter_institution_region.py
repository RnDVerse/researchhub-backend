# Generated by Django 4.1 on 2024-05-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("institution", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="city",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="institution",
            name="region",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
