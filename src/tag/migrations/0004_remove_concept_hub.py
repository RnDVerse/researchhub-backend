# Generated by Django 4.1 on 2023-09-08 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0003_concept_hub"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="concept",
            name="hub",
        ),
    ]